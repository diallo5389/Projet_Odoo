from odoo import fields, models

class ModelProprietesTags(models.Model):
    _name = "domaines_proprietes_tags"
    _description = "Table containing des tags"
    _order = "name"

    name = fields.Char(string="Name",required=True)
    couleur = fields.Integer()

    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'Each name must be unique.'),
    ]