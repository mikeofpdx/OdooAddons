# -*- coding: utf-8 -*-
{
    'name': "Engineering Product Tab",
    'version': "1.0",
    'category': 'Manufacturing',
    'summary': "Adds an Engineering tab to Products using default_code as PLM Part Number",
    'description': """
Engineering Product Tab for Odoo 18

- Uses default_code as PLM Part Number
- Adds Engineering, ECAD Mapping, Electrical Characteristics, and Notes sections
- No extra fields created for PLM Part Number
""",
    'author': "MikeofPdx",
    'depends': ['product'],
    'data': [
        'views/product_template_views.xml',
        'views/engineering_mass_edit_wizard_view.xml',
        'views/server_action.xml'
    
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
