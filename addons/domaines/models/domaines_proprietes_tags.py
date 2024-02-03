from odoo import fields, models

class ModelProprietesTags(models.Model):
    _name = "domaines_proprietes_tags"
    _description = "Table containing des tags"

    name = fields.Char(string="Name",required=True)