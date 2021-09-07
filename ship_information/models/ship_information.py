# -*- coding: utf-8 -*-
from odoo import fields, models


class ShipInformation(models.Model):
    _name = "ship.information"
    _inherit = ['mail.thread']
    _description = "Ship information"
    _rec_name = "imo"
    imo = fields.Char(string="Imo Number")
    _sql_constraints = [('field_unique', 'unique(imo)', 'Choose another value - Imo Number has to be unique!')]
    responsible_id = fields.Many2one(comodel_name="res.partner", string="responsible")
    ship_yard = fields.Char(string='Ship yard', related="responsible_id.ship_yards", required=True, tracking=True)
    ship_owner = fields.Char(string='Ship owner', related="responsible_id.ship_owners", required=True, tracking=True)
    ship_management = fields.Char(string='Ship management', related="responsible_id.ship_managements", required=True, tracking=True)
    engine_builder = fields.Char(string='Engine builder', related="responsible_id.engine_builders", required=True, tracking=True)
    hull_number = fields.Char(string='Hull Number', required=True, tracking=True)
    engine_number = fields.Char(string='Engine Number', required=True, tracking=True)
    vessel_name = fields.Char(string='Vessel Name', required=True, tracking=True)
    build_year = fields.Char(string='Build Year', required=True, tracking=True)
