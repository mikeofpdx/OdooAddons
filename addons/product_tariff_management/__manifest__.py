{
    'name': 'Product Tariff Management',
    'version': '18.0.0.0',
    'category': 'Inventory/Purchase',
    'summary': 'Adds HS Codes and Tariff Rates to Products and POs',
    'depends': ['product', 'purchase'],
    'data': [
        'views/product_views.xml',
        'views/report_purchase_quotation.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
}