# Product Environmental Compliance Module

This Odoo module adds environmental compliance tracking to products. It allows you to store compliance statuses (RoHS, REACH, CA Prop 65) and attach related documents to each product.

---

## Features

- **Compliance Fields** on `product.template`:
  - RoHS Compliance (`compliance_rohs`)
  - REACH Compliance (`compliance_reach`)
  - CA Prop 65 Compliance (`compliance_prop65`)
  
- **Attachments**:
  - Many2many field for attaching compliance documents (`compliance_attachment_ids`)
  - View and download attached documents via "View/Download Documents" button

- **Access Control**:
  - Compliance documents are visible to all users by default.
  - Optional `groups` can be set to restrict access.

---

## Installation

1. Copy the module folder into your Odoo `addons` directory (e.g., `/mnt/extra-addons/product_env_compliance`).
2. Restart the Odoo server.
3. Update the apps list in Odoo (`Apps -> Update Apps List`).
4. Install the `Product Environmental Compliance` module.

---

## Usage

1. Navigate to a product (`Sales -> Products`).
2. Go to the product form view.
3. Click on the **Environmental Compliance** tab:
   - Set compliance statuses.
   - Attach compliance documents using the tags field.
4. Click **View/Download Documents** to open a filtered view of attachments.

---

## Notes

- This module inherits the standard `product.template` model.
- The "View/Download Documents" button uses a Python method (`action_view_compliance_docs`) to filter attachments for the current product.
- No additional `ir.actions.act_window` records are required.
- The many2many attachments field uses `many2many_tags` widget.

---

## Development

- Written for **Odoo 18**.
- Python file: `models/product_template.py`
- XML view file: `views/product_env_compliance_view.xml`

---

## License

MIT License
