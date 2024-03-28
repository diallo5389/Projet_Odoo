from odoo import fields, models, api, Command
from odoo.exceptions import UserError,ValidationError

class ModelProprietes(models.Model):
    _inherit = "domaines_proprietes"

    def Sold_action(self):
        print("Methode de la fonction fils")
        self.env["account.move"].create({
            "partner_id": self.buyer_id.id,
            "move_type":"out_invoice",
            #"journal_id":???????,
            "name": self.name,
            "invoice_line_ids": [
                Command.create({
                    "name":self.description,
                    'quantity': 1.0,
                    'price_unit': self.selling_price + self.selling_price*0.06 + 100.00,
                }),
            ],
                })
        return super().Sold_action()