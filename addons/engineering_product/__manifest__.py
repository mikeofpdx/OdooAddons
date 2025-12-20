# -*- coding: utf-8 -*-
{
    'name': 'Engineering Product Extension',
    'version': '18.0.1.1.1',
    'category': 'Engineering/Product',
    'summary': 'Electronic component attributes and ECAD library management',
    'description': """
    Engineering Product Integration & ECAD Library Management
    ==========================================================

    This module bridges the gap between hardware engineering and ERP data management. 
    It extends the standard Odoo product catalog to support technical electronics 
    specifications and introduces a robust lifecycle management system.

    Key Highlights:
    ---------------
    * **Engineering Attributes:** Track Symbols, Packages, MPN, Value, Tolerance, 
    Power, and Voltage ratings directly on the product.
    * **ECAD Library Management:** Organize products into specific engineering 
    libraries with a dedicated many-to-one relationship.
    * **Lifecycle Workflow:** Transition parts from Draft to Prototype, Production, 
    or Obsolete.
    * **Data Integrity:** Automatically locks technical specifications for 
    editing once a part is moved past the 'Draft' stage.
    * **Optimized UX:** Custom search filters to identify unassigned parts 
    and color-coded status indicators in list views.
    """,
    'author': 'MikeofPDX',
    'website': 'https://github.com/mikeofpdx/OdooAddons',
    'category': 'Engineering/Product',
    'depends': ['base', 'product', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/engineering_ecad_library_views.xml',
        'views/product_template_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}