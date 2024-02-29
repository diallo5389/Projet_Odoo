from odoo import fields, models

class ModelUsersHerited(models.Model):
    _inherit = 'res.users'
    property_ids = fields.One2many(comodel_name="domaines_proprietes", inverse_name="salesman_id", domain=[('state_of_sale', 'in', ['New','Offer Received'])], string="Properties")