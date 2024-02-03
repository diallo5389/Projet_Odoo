from odoo import fields, models

class ModelProprietesOffer(models.Model):
    _name = "domaines_proprietes_offer"
    _description = "Table containing offers"

    price = fields.Float(string="Price")
    status = fields.Selection(string="Status", selection=[("Processing","Processiong"),("Accepted","Accepted"),("Refused","Refused")],copy=False)
    partner_id = fields.Many2one("res.partner", string="Partner",required=True)
    property_id = fields.Many2one("domaines_proprietes",required=True)