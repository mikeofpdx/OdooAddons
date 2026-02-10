{
    'name': 'Product Manufacturer Search Extension',
    'version': '18.0.1.0.0',
    'category': 'Product',
    'summary': 'Adds manufacturer search capabilities to the product catalog',
    'depends': [
        'product', 
        'product_manufacturer' # <--- Dependency on the OCA module
    ],
    'data': [
        'views/product_template_views.xml',
    ],
    'installable': True,
}
