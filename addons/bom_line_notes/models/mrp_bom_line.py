from odoo import fields, models


class MrpBomLine(models.Model):
    _inherit = 'mrp.bom.line'

    notes = fields.Text(
        string='Notes',
        help='Additional notes or comments for this BOM line'
    )