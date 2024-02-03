from odoo import fields, models
from datetime import timedelta  

class ModelProprietes(models.Model):
    _name = "domaines_proprietes"
    _description = "Ventes et gestion de domaines"

    
    name =  fields.Char(string='Name',required=True)
    description = fields.Text(string='Description')
    property_type_id = fields.Many2one("domaines_proprietes_types", string="Property Type")
    properties_tags_id = fields.Many2many("domaines_proprietes_tags", required=True)
    salesman_id = fields.Many2one("res.users", string="Salesman",default=lambda self: self.env.user)
    buyer_id = fields.Many2one("res.partner", string="Buyer",copy=False)
    offer_id = fields.One2many("domaines_proprietes_offer","property_id")
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(default=fields.Date.today() + timedelta(days=90),copy=False)
    expected_price = fields.Float(string='Expected Price',required=True) 
    selling_price = fields.Float(string='Selling Price',copy=False,readonly=True)
    bedrooms = fields.Integer(default=2,string='Bedrooms')
    living_area = fields.Integer(string='Living Area')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage')
    garden_area = fields.Integer(string='Garden Area')
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('North','North'), ('South','South'), ('East','Eest'), ('West','West')]
    )
    state_of_sale = fields.Selection(
        default="New",
        string='State',
        copy=False,
        required=True,
        selection=[('New','New'), ('Offer Received','Offer Received'), ('Offer Accepted','Offer Accepted'), ('Sold','Sold'), ('Canceled','Canceled')]
    )
    active = fields.Boolean(default=True)