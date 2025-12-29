{
    'name': 'Product Datasheets',
    'version': '18.0.1.0.1',
    'category': 'Inventory',
    'summary': 'Manage shared datasheets for products',
    'description': """
        This module allows you to:
        - Create datasheet records that can be shared across multiple products
        - Link products to datasheets (many2many relationship)
        - Upload one datasheet PDF and reference it from thousands of parts
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['product'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_datasheet_views.xml',
        'views/product_template_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}