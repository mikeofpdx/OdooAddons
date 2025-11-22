{
    "name": "Product Environmental Compliance",
    "version": "18.0.1.0.1",
    "summary": "Adds environmental compliance tracking and attachments to products",
    "description": """
Adds an Environmental Compliance tab to products for:
 • RoHS, REACH, and Prop 65 compliance (Yes/No/Exempt/Unknown)
 • Linked compliance documents (shared across products)
""",
    "author": "Tall Timber IT",
    "category": "Product",
    'summary': 'Track environmental compliance and attach related documents to products',
    "depends": ["product"],
    "data": [
        "views/product_env_compliance_view.xml",
    ],
    "installable": True,
    "application": False,
    "license": "LGPL-3",
}

