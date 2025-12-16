from odoo import fields, models


class EcadLibrary(models.Model):
    _name = "engineering.ecad.library"
    _description = "ECAD Library"
    _order = "name"

    name = fields.Char(
        string="Library Name",
        required=True
    )

    filename = fields.Char(
        string="Library File",
        required=True,
        help="Fusion 360 Electronics .lbr filename"
    )
    
    product_ids = fields.One2many(
        'product.template',
        'ecad_library_id',
        string='Products'
    )
    
    description = fields.Text()

    active = fields.Boolean(default=True)

    _sql_constraints = [
        (
            "filename_unique",
            "unique(filename)",
            "ECAD library filename must be unique.",
        ),
    ]
