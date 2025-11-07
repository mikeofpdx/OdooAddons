
{
    'name': 'BOM Line Notes',
    'version': '18.0.1.0.0',
    'category': 'Manufacturing',
    'summary': 'Add notes field to BOM lines',
    'description': """
        This module adds a notes field to Bill of Materials lines.
        The notes field is visible in all BOM views (form, tree, kanban).
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'license': 'LGPL-3',
    'depends': ['mrp'],
    'data': [
        'views/mrp_bom_line_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}