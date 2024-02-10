from odoo import fields, models

class ModelProprietesTypes(models.Model):
    _name = "domaines_proprietes_types"
    _description = "Table containing the type of properties"

    name = fields.Char(string="Name",required=True)

    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'Each name must be unique.'),
    ]