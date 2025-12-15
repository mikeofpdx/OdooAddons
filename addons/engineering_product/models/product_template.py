from odoo import api, fields, models
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = "product.template"

    # -------------------------
    # Lifecycle / Governance
    # -------------------------
    lifecycle = fields.Selection(
        [
            ("draft", "Draft"),
            ("active", "Active"),
            ("nrnd", "NRND"),
            ("obsolete", "Obsolete"),
        ],
        string="Lifecycle",
        default="draft",
        tracking=True,
    )

    library_owner = fields.Many2one(
        "res.users",
        string="Library Owner",
        help="Engineer responsible for this part definition",
    )

    eco_reference = fields.Char(
        string="ECO / Change Reference",
        help="Engineering change order or ticket reference",
    )

    # -------------------------
    # ECAD Mapping
    # -------------------------
    ecad_library_id = fields.Many2one(
        "engineering.ecad.library",
        string="ECAD Library",
        required=True,
        help="Fusion 360 Electronics library that owns this part",
    )

    ecad_device = fields.Char(
        string="ECAD Device",
        help="Fusion/EAGLE device name",
    )

    ecad_package = fields.Char(
        string="ECAD Package",
        help="Fusion/EAGLE footprint / package name",
    )

    footprint_rev = fields.Char(
        string="Footprint Revision",
        help="Internal footprint revision identifier",
    )

    # -------------------------
    # Electrical Characteristics
    # -------------------------
    value = fields.Char(string="Value")
    tolerance = fields.Char(string="Tolerance")
    power_rating = fields.Char(string="Power Rating")
    voltage_rating = fields.Char(string="Voltage Rating")
    part_type = fields.Char(string="Part Type")

    # -------------------------
    # Notes / Commentary
    # -------------------------
    engineering_notes = fields.Text(
        string="Engineering Notes",
        help="Design rationale, constraints, validation notes",
    )

    ecad_library_notes = fields.Text(
        string="ECAD Library Notes",
        help="Notes specific to ECAD symbol/device/package usage",
    )

    # -------------------------
    # Constraints
    # -------------------------
    _sql_constraints = [
        (
            "default_code_unique",
            "unique(default_code)",
            "PLM Part Number must be unique.",
        ),
    ]

    # -------------------------
    # Immutability Rules
    # -------------------------
    @api.constrains("default_code", "lifecycle")
    def _check_plm_pn_immutability(self):
        for rec in self:
            if not rec._origin:
                continue

            if (
                rec._origin.lifecycle != "draft"
                and rec.default_code != rec._origin.default_code
            ):
                raise ValidationError(
                    "PLM Part Number cannot be changed once the lifecycle "
                    "is no longer Draft."
                )

    @api.constrains("ecad_library_id", "ecad_device", "ecad_package", "lifecycle")
    def _check_ecad_mapping_immutability(self):
        for rec in self:
            if not rec._origin:
                continue

            if rec._origin.lifecycle != "draft":
                if rec.ecad_library_id != rec._origin.ecad_library_id:
                    raise ValidationError(
                        "ECAD Library cannot be changed after Draft."
                    )
                if rec.ecad_device != rec._origin.ecad_device:
                    raise ValidationError(
                        "ECAD Device cannot be changed after Draft."
                    )
                if rec.ecad_package != rec._origin.ecad_package:
                    raise ValidationError(
                        "ECAD Package cannot be changed after Draft."
                    )
