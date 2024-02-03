from odoo import fields, models

class ModelProprietesTypes(models.Model):
    _name = "domaines_proprietes_types"
    _description = "Table containing the type of properties"

    name = fields.Char(string="Name",required=True)

