from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = "product.template"

    # Compliance fields
    compliance_rohs = fields.Selection(
        [("yes","Yes"),("no","No"),("exempt","Exempt"),("unknown","Unknown")],
        default="unknown",
        string="RoHS Compliance"
    )
    compliance_reach = fields.Selection(
        [("yes","Yes"),("no","No"),("exempt","Exempt"),("unknown","Unknown")],
        default="unknown",
        string="REACH Compliance"
    )
    compliance_prop65 = fields.Selection(
        [("yes","Yes"),("no","No"),("exempt","Exempt"),("unknown","Unknown")],
        default="unknown",
        string="CA Prop 65 Compliance"
    )

    # Many2many attachments
    compliance_attachment_ids = fields.Many2many(
        "ir.attachment",
        "product_compliance_attachment_rel",
        "product_id",
        "attachment_id",
        string="Compliance Documents"
    )

    # Button action to view attachments
    def action_view_compliance_docs(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "Compliance Documents",
            "res_model": "ir.attachment",
            "views": [
                (self.env.ref("product_env_compliance.view_compliance_attachment_list").id, "list"),
                (False, "kanban"),
                (False, "form"),
            ],
            "domain": [("id", "in", self.compliance_attachment_ids.ids)],
            "target": "current",
        }
