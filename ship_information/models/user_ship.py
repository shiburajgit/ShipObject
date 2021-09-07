# -*- coding: utf-8 -*-
from odoo import fields, models


class UserShip(models.Model):
    _inherit = "res.partner"
    ship_yards = fields.Char(string='Ship yard')
    ship_owners = fields.Char(string='Ship owner')
    ship_managements = fields.Char(string='Ship management')
    engine_builders = fields.Char(string='Engine builder')
