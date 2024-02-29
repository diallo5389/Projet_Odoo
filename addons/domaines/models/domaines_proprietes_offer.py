from odoo import fields, models,api
from datetime import timedelta 
from odoo.exceptions import UserError, ValidationError

class ModelProprietesOffer(models.Model):
    _name = "domaines_proprietes_offer"
    _description = "Table containing offers"
    _order = "price desc"

    price = fields.Float(string="Price")
    status = fields.Selection(string="Status",default="Processing", selection=[("Processing","Processing"),("Accepted","Accepted"),("Refused","Refused")],copy=False)
    validity = fields.Integer(string="Validity (days)", default=7)
    deadline = fields.Date(string="Deadline", compute = "_deadline", inverse = "_inverse_deadline")
    partner_id = fields.Many2one("res.partner", string="Partner",required=True)
    property_id = fields.Many2one("domaines_proprietes",required=True)
    confirmed = fields.Boolean()
    property_type_id = fields.Many2one(related = "property_id.property_type_id", store=True)

    @api.depends("validity")
    def _deadline(self):
        for record in self:
            record.deadline = fields.Date.today() + timedelta(days=record.validity)
            if record.create_date:
                record.deadline = record.create_date + timedelta(days=record.validity)

    def _inverse_deadline(self):
        for record in self:
            if record.create_date:
                record.validity = (record.deadline - record.create_date.date()).days

    def action_confirm(self):    
        parent_record = self.env['domaines_proprietes'].search([('offer_id', '=', self.id)], limit=1)
        offers = parent_record.offer_id
        for offer in offers :
            if offer.id != self.id and offer.confirmed :
                raise UserError(f"Une offre est déjà acceptée. Veuillez d'abord la refuser avant d'accepter une autre {offer.id}")
        self.confirmed = True
        if parent_record:
            parent_record.buyer_id = self.partner_id
            parent_record.selling_price = self.price
            self.status = "Accepted"
        
    def action_refuse(self):
        parent_record = self.env['domaines_proprietes'].search([('offer_id', '=', self.id)], limit=1)
        if parent_record:
            self.status = "Refused"
            if self.confirmed :
                parent_record.buyer_id = ""
                parent_record.selling_price = 0.0
            self.confirmed = False

    #Contraintes SQL (plus performant en terme de ressources que les contraintes python)
    _sql_constraints = [
        ('check_positive', 'CHECK(price > 0.0 )','The offer must be positif.')
    ]  
    
    #Contrainte en python (équivalent au "_sql_constraints")
    # @api.constrains('price')
    # def _selling_price(self):
    #     if self.price <= 0.0 :
    #         raise ValidationError("The offer must be positif.")

    @api.model
    def create(self,vals):
        propriete_parent = self.env['domaines_proprietes'].browse(vals['property_id']) #Recherche de la propriété pour laquelle l'offre est en train d'être créée
        for record in propriete_parent.offer_id :
            if record :     
                if record.price > vals['price']:
                    raise UserError(f"Des offres supérieures à {vals['price']} GNF existent déjà !")
        if propriete_parent.state_of_sale == "New":
            propriete_parent.state_of_sale = "Offer Received"
        return super().create(vals)
    
    #Pas parvenu à mettre "New" sur le statut de la propriété lors de la suppression de la dernière offre d'une propriété
    # @api.ondelete(at_uninstall=False)
    # def _offres_existes(self):
    #     propriete_parent = self.env['domaines_proprietes'].browse(self.property_id) #Recherche de la propriété pour laquelle l'offre est en train d'être supprimée
    #     for record in propriete_parent.offer_id :
    #         print(f"{record}Bonjourrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
    #     raise UserError(f"Finnnnnnnnnnnnnnnnn!")
        # if len(propriete_parent.offer_id) <= 1 :
        #     propriete_parent.state_of_sale = "New"