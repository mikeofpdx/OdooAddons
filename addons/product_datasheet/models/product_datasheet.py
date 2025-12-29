from odoo import models, fields, api

class ProductDatasheet(models.Model):
    _name = 'product.datasheet'
    _description = 'Product Datasheet'
    _order = 'name'

    name = fields.Char(string='Datasheet Name', required=True, index=True)
    manufacturer = fields.Char(string='Manufacturer')
    part_number = fields.Char(string='Manufacturer Part Number', index=True)
    description = fields.Text(string='Description')
    
    # File attachment
    datasheet_file = fields.Binary(string='Datasheet File', attachment=True)
    datasheet_filename = fields.Char(string='Filename')
    
    # Or use existing attachment
    attachment_id = fields.Many2one('ir.attachment', string='Attachment')
    
    # Link to products
    product_ids = fields.Many2many(
        'product.template',
        'product_datasheet_rel',
        'datasheet_id',
        'product_id',
        string='Products'
    )
    product_count = fields.Integer(
        string='Number of Products',
        compute='_compute_product_count'
    )
    
    # Additional fields
    revision = fields.Char(string='Revision')
    date_issued = fields.Date(string='Date Issued')
    url = fields.Char(string='External URL')
    active = fields.Boolean(default=True)

    @api.depends('product_ids')
    def _compute_product_count(self):
        for record in self:
            record.product_count = len(record.product_ids)

    def action_view_products(self):
        """Action to view all products using this datasheet"""
        self.ensure_one()
        return {
            'name': 'Products',
            'type': 'ir.actions.act_window',
            'res_model': 'product.template',
            'view_mode': 'list,form',
            'domain': [('id', 'in', self.product_ids.ids)],
            'context': {'default_datasheet_ids': [(4, self.id)]},
        }
    def action_view_datasheet(self):
        self.ensure_one()

        # 1) Prefer explicit attachment
        if self.attachment_id:
            return {
                'type': 'ir.actions.act_url',
                'url': f'/web/content/{self.attachment_id.id}?download=false',
                'target': 'new',
            }

        # 2) Fallback to binary field
        if self.datasheet_file:
            return {
                'type': 'ir.actions.act_url',
                'url': f'/web/content/{self._name}/{self.id}/datasheet_file'
                    f'?filename={self.datasheet_filename}&download=false',
                'target': 'new',
            }

    return False
