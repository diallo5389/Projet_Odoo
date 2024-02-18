from odoo import fields, models, api   
from odoo.exceptions import UserError 

class ModelProprietesTypes(models.Model):
    _name = "domaines_proprietes_types"
    _description = "Table containing the type of properties"
    _order = "name"

    name = fields.Char(string="Name",required=True)
    property_ids = fields.One2many("domaines_proprietes","property_type_id")
    propiretes_offer_id = fields.One2many("domaines_proprietes_offer","property_type_id")
    offer_count = fields.Integer(compute="_nombre_offres")
    
    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'Each name must be unique.'),
    ]

    @api.depends("propiretes_offer_id")
    def _nombre_offres(self):
        self.offer_count  = len(self.propiretes_offer_id)
        #raise UserError({self.propiretes_offer_id})
