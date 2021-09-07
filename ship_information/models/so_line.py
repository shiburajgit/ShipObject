# -*- coding: utf-8 -*-
from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    ship_information_id = fields.Many2one(comodel_name="ship.information", string='Ship Information')
