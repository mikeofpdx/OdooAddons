from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # Lifecycle Status
    lifecycle = fields.Selection([
        ('draft', 'Draft'),
        ('prototype', 'Prototype'),
        ('production', 'Production'),
        ('obsolete', 'Obsolete')
    ], string='Lifecycle Status', default='draft', required=True, tracking=True)
    
    # ECAD Data
    ecad_library_id = fields.Many2one('engineering.ecad.library', string='ECAD Library', ondelete='set null')
    ecad_symbol = fields.Char(string='ECAD Device')
    ecad_package = fields.Char(string='ECAD Package')

    # Component Specifications
    value = fields.Char(string='Value')
    tolerance = fields.Char(string='Tolerance')
    power_rating = fields.Char(string='Power Rating')
    voltage_rating = fields.Char(string='Voltage Rating')
    part_type = fields.Char(string='Part Type')

    ecad_library_assigned = fields.Boolean(
        compute='_compute_ecad_library_assigned',
        store=True,
        index=True
)
    @api.depends('ecad_library_id')
    def _compute_ecad_library_assigned(self):
        for product in self:
            product.ecad_library_assigned = bool(product.ecad_library_id)

        
    def action_open_record(self):
        """Opens the specific product form view"""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'product.template',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'current',
        }
            