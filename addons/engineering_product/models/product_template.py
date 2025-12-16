# -*- coding: utf-8 -*-
from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # Optional engineering fields
    lifecycle = fields.Selection([
        ('design', 'Design'),
        ('prototype', 'Prototype'),
        ('production', 'Production'),
        ('obsolete', 'Obsolete')
    ], string="Lifecycle")

    library_owner = fields.Many2one('res.users', string="Library Owner")
    eco_reference = fields.Char(string="ECO Reference")

    ecad_library_id = fields.Many2one('engineering.ecad.library', string="ECAD Library")
    ecad_device = fields.Char(string="ECAD Device")
    ecad_package = fields.Char(string="ECAD Package")
    footprint_rev = fields.Char(string="Footprint Revision")

    value = fields.Float(string="Value")
    tolerance = fields.Char(string="Tolerance")
    power_rating = fields.Char(string="Power Rating")
    voltage_rating = fields.Char(string="Voltage Rating")
    part_type = fields.Char(string="Part Type")

    engineering_notes = fields.Text(string="Engineering Notes")
    ecad_library_notes = fields.Text(string="ECAD Library Notes")
