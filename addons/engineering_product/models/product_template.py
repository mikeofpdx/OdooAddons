from odoo import models, fields, api
from odoo.osv import expression

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
    ecad_deviceset = fields.Char(string='ECAD Device Set') #map to DEVICESET in Eagle/Fusion360
    ecad_symbol = fields.Char(string='ECAD Device') #map to DEVICE in Eagle/Fusion360
    ecad_package = fields.Char(string='ECAD Package') #map to PACKAGE in Eagle/Fusion360

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
            
    @api.model
    def ecad_resolve_v1(self, criteria):
        """
        Resolve ECAD intent into concrete Odoo parts.

        criteria = {
            'ecad_library': 'Resistors.lbr',
            'ecad_deviceset': 'RES',
            'ecad_symbol': '0402',
            'ecad_package': 'RESC1005X40',
            'value': '100R',
            'tolerance': '1%',
            'power_rating': '0.1W',
            'voltage_rating': None,
            'part_type': 'Thin Film',
            'lifecycle': 'production'
        }
        """

        domain = [
            ('ecad_library_id.name', '=', criteria.get('ecad_library')),
            ('ecad_deviceset', '=', criteria.get('ecad_deviceset')),
            ('ecad_symbol', '=', criteria.get('ecad_symbol')),
            ('ecad_package', '=', criteria.get('ecad_package')),
            ('lifecycle', '!=', 'obsolete'),
        ]

        # Optional constraints
        optional_fields = [
            'value',
            'tolerance',
            'power_rating',
            'voltage_rating',
            'part_type',
            'lifecycle',
        ]

        for field in optional_fields:
            if criteria.get(field):
                domain.append((field, 'ilike', criteria[field]))

        products = self.search(domain)

        result = []
        for product in products:
            result.append({
                'id': product.id,
                'part_number': product.default_code,
                'name': product.name,
                'value': product.value,
                'tolerance': product.tolerance,
                'part_type': product.part_type,
                'power_rating': product.power_rating,
                'voltage_rating': product.voltage_rating,
                'lifecycle': product.lifecycle,
                'inventory': product.qty_available,
                'cost': product.standard_price,
                'odoo_url': (
                    f"/web#id={product.id}"
                    f"&model=product.template"
                    f"&view_type=form"
                )
            })

        return {
            'api_version': '1.0',
            'status': 'success',
            'count': len(result),
            'results': result
        }