from odoo import fields, models

class ModelProprietes(models.Model):
    _name = "domaines_proprietes"
    _description = "Ventes et gestion de domaines"

    name =  fields.Char(string='Nom',required=True) #required=True fait en sorte que ce champs ne puisse pas etre vide
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(year=2024,month=1,day=1) # La date doit obligatoirement etre initialisée
    expected_price = fields.Float(string='Expected Price')
    selling_price = fields.Float(string='Selling Price',required=True) 
    bedrooms = fields.Integer(string='Bedrooms')
    living_area = fields.Integer(string='Living Area')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Integer(string='Garden Area')
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('North','NORTH'), ('South','SOUTH'), ('East','EAST'), ('West','WEST')]
    )
