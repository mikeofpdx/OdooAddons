import io
import csv
import base64
from odoo import models, fields, api
from odoo.osv import expression


class EngineeringEcadLibrary(models.Model):
    _name = 'engineering.ecad.library'
    _description = 'Engineering ECAD Library'
    _order = 'name'

    name = fields.Char(string='Library Name', required=True, index=True)
    code = fields.Char(string='Library Code', required=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(default=True)

    # Link to products
    product_ids = fields.One2many(
        'product.template',
        'ecad_library_id',
        string='Products'
    )
    product_count = fields.Integer(
        string='Number of Products',
        compute='_compute_product_count'
    )
    @api.depends('product_ids')
    def _compute_product_count(self):
        for record in self:
            record.product_count = len(record.product_ids)
    
            
    def action_view_products(self):
        """Action to view all products using this library"""
        self.ensure_one()
        return {
            'name': 'Products',
            'type': 'ir.actions.act_window',
            'res_model': 'product.template',
            'view_mode': 'list,form',
            'domain': [('ecad_library_id', '=', self.id)],
        }
    
    # Export library to CSV for ECAD import    
    def action_export_library_to_csv(self):
        self.ensure_one()
        output = io.StringIO()
        writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        # Header Row - Tailored for ECAD Import
        writer.writerow(['Library', 'Part_Number', 'DeviceSet', 'Symbol', 'Footprint', 'Value', 'Tolerance', 'Voltage_Rating', 'Power_Rating', 'Lifecycle', 'Part_Type'])
        
        # Loop through the products linked to THIS library
        for product in self.product_ids:
            writer.writerow([
                self.code or '',
                product.default_code or '',
                product.ecad_deviceset or '',
                product.ecad_symbol or '',
                product.ecad_package or '',
                product.value or '',
                product.tolerance or '',
                product.voltage_rating or '',
                product.power_rating or '',
                product.lifecycle or '',
                product.part_type or ''
            ])
        
        # Prepare the file download
        data = output.getvalue().encode('utf-8')
        # Using the code in the filename makes it easy to archive
        filename = f"Library_{self.code or 'Export'}.csv"
        
        attachment = self.env['ir.attachment'].create({
            'name': filename,
            'type': 'binary',
            'datas': base64.b64encode(data),
            'mimetype': 'text/csv',
        })
        
        return {
            'type': 'ir.actions.act_url',
            'url': f'/web/content/{attachment.id}?download=true',
            'target': 'new',
        }

    def action_export_all_libraries_to_csv(self):
        """
        Export ALL products assigned to ANY ECAD library into one CSV file
        """
        output = io.StringIO()
        writer = csv.writer(
            output,
            delimiter=',',
            quotechar='"',
            quoting=csv.QUOTE_MINIMAL
        )

        # Header Row (same as single-library export)
        writer.writerow([
            'Library',
            'Part_Number',
            'DeviceSet',
            'Symbol',
            'Footprint',
            'Value',
            'Tolerance',
            'Voltage_Rating',
            'Power_Rating',
            'Lifecycle',
            'Part_Type'
        ])

        # Fetch all products assigned to a library
        products = self.env['product.template'].search([
            ('ecad_library_id', '!=', False)
        ])

        for product in products:
            writer.writerow([
                product.ecad_library_id.code or '',
                product.default_code or '',
                product.ecad_deviceset or '',
                product.ecad_symbol or '',
                product.ecad_package or '',
                product.value or '',
                product.tolerance or '',
                product.voltage_rating or '',
                product.power_rating or '',
                product.lifecycle or '',
                product.part_type or '',
            ])

        data = output.getvalue().encode('utf-8')
        filename = "odoo_export.csv"

        attachment = self.env['ir.attachment'].create({
            'name': filename,
            'type': 'binary',
            'datas': base64.b64encode(data),
            'mimetype': 'text/csv',
        })

        return {
            'type': 'ir.actions.act_url',
            'url': f'/web/content/{attachment.id}?download=true',
            'target': 'new',
        }

    
    
    @api.model
    def _search_display_name(self, operator, value, *args, **kwargs):
        """
        Odoo 18 Universal Signature. 
        Accepts any number of arguments to prevent 'unexpected keyword' errors.
        """
        if operator in ('like', 'ilike', '=like', '=ilike'):
            domain = kwargs.get('domain', [])
            search_domain = ['|', ('name', operator, value), ('code', operator, value)]
            return expression.AND([domain, search_domain])
        return super()._search_display_name(operator, value, *args, **kwargs)