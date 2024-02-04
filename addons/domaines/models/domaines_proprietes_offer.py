from odoo import fields, models,api
from datetime import timedelta 

class ModelProprietesOffer(models.Model):
    _name = "domaines_proprietes_offer"
    _description = "Table containing offers"

    price = fields.Float(string="Price")
    status = fields.Selection(string="Status", selection=[("Processing","Processing"),("Accepted","Accepted"),("Refused","Refused")],copy=False)
    validity = fields.Integer(string="Validity (days)", default=7)
    deadline = fields.Date(string="Deadline", compute = "_deadline", inverse = "_inverse_deadline")
    partner_id = fields.Many2one("res.partner", string="Partner",required=True)
    property_id = fields.Many2one("domaines_proprietes",required=True)

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