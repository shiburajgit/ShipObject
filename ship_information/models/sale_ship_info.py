# -*- coding: utf-8 -*-
from odoo import fields, models


class SaleShip(models.Model):
    _inherit = "sale.order"
    ship_id = fields.Many2one(comodel_name="ship.information", string='Ship Information')
    project = fields.Char(string="Project")
    contract_no = fields.Char(string="Contract No")
    purchase_ids = fields.One2many('purchase.order', 'related_sale_order_id')

    # @api.onchange('ship_id')
    # def onchange_ship_id(self):
    #     if self.ship_id:
    #         self.order_line.ship_information_id = self.ship_id.id
    #     else:
    #         self.order_line.ship_information_id = ''

    def update_ship(self):
        if self.ship_id:
            print("self", self)
            print(self.ship_id.id)
            self.order_line.ship_information_id = self.ship_id.id
