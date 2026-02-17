from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    hs_tariff_code = fields.Char(string="HS Tariff Code")
    tariff_rate = fields.Float(string="Tariff Rate (%)", help="Enter the percentage rate (e.g., 15.0)")