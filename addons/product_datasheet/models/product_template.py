from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    datasheet_ids = fields.Many2many(
        'product.datasheet',
        'product_datasheet_rel',
        'product_id',
        'datasheet_id',
        string='Datasheets'
    )
    
    datasheet_count = fields.Integer(
        string='Datasheet Count',
        compute='_compute_datasheet_count'
    )

    def _compute_datasheet_count(self):
        for product in self:
            product.datasheet_count = len(product.datasheet_ids)

    def action_view_datasheets(self):
        """Action to view datasheets for this product"""
        self.ensure_one()
        return {
            'name': 'Datasheets',
            'type': 'ir.actions.act_window',
            'res_model': 'product.datasheet',
            'view_mode': 'list,form',
            'domain': [('id', 'in', self.datasheet_ids.ids)],
        }
