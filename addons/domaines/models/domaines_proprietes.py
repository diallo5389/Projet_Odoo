from odoo import fields, models,api
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
    best_offer = fields.Float(compute="_best_offer",string="Best Offer")
    bedrooms = fields.Integer(default=2,string='Bedrooms')
    facades = fields.Integer(string='Facades')
    living_area = fields.Integer(string='Living Area')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string="Garden", default=False)
    garden_area = fields.Integer(string='Garden Area')
    total_area = fields.Float(compute="_total_area_methode",string="Total Area") 
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

    @api.depends("living_area","garden_area")
    def _total_area_methode(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends("offer_id.price")
    def _best_offer(self):
        for record in self:
            record.best_offer = 0.0
            prices = record.mapped("offer_id.price")
            if prices:
                record.best_offer = max(prices)

    @api.onchange("garden")
    def _garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation ="North"
        else:
            self.garden_area = 0
            self.garden_orientation = ""