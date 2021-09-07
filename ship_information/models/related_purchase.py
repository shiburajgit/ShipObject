# -*- coding: utf-8 -*-
from odoo import fields, models


class PurchaseContract(models.Model):
    _inherit = "purchase.order"
    related_sale_order_id = fields.Many2one(comodel_name="sale.order", string='Related sale order')
    purchase_contract_no = fields.Char(string="Contract No", related="related_sale_order_id.contract_no")


