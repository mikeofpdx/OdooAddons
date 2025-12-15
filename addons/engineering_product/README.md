# Engineering Product Extension for Odoo 18

This repository contains a professional-grade Odoo 18 addon that extends the standard product model to support **engineering, ECAD, and PLM-aligned metadata** without breaking Odoo core behavior.

It is designed for organizations where:

* Part numbers are mastered in an **external PLM system**
* Odoo acts as **ERP / MRP / inventory of record**
* ECAD libraries (Fusion 360 Electronics / Eagle) must remain synchronized
* Parts must be **mass-updated safely** without duplication

---

## ✨ Key Features

* Adds **engineering attributes** to `product.template`
* Supports **ECAD library targeting** (which `.lbr` a part belongs to)
* Enforces **PLM-safe constraints** (immutability after lifecycle release)
* Fully compatible with **Odoo 18 List View / Server Actions**
* No fork of core models
* No change to existing product numbering

---

## 🧠 Design Philosophy

This addon follows several non-negotiable principles:

1. **Odoo is not the PLM**
   Part numbers, lifecycle authority, and release decisions originate elsewhere.

2. **ERP data must remain mutable — until it must not**
   Draft parts are flexible. Released parts are locked.

3. **ECAD libraries are explicit, not implicit**
   Every electronic part must know which Fusion 360 Electronics library it belongs to.

4. **Bulk updates must be safe and auditable**
   No imports. No duplication. No SQL hacks.

---

## 📦 Module Overview

### Module Name

```
engineering_product
```

### Depends On

* `product`
* `base`

---

## 🗂 Models

### `engineering.ecad.library`

Defines a controlled list of ECAD libraries that correspond to Fusion 360 Electronics `.lbr` files.

| Field         | Type    | Description                                  |
| ------------- | ------- | -------------------------------------------- |
| `name`        | Char    | Human-readable name                          |
| `code`        | Char    | Short identifier (used in automation/export) |
| `description` | Text    | Optional notes                               |
| `active`      | Boolean | Soft-delete support                          |

Libraries are user-manageable and auditable.

---

### `product.template` (Extended)

Adds engineering-specific fields without altering core behavior.

| Field             | Type      | Description                               |
| ----------------- | --------- | ----------------------------------------- |
| `plm_pn`          | Char      | External PLM part number (reference only) |
| `lifecycle`       | Selection | Draft / Active / Obsolete                 |
| `ecad_library_id` | Many2one  | Target ECAD library                       |
| `ecad_package`    | Char      | Footprint/package name                    |
| `ecad_symbol`     | Char      | Symbol name                               |
| `ecad_device`     | Char      | Device/technology identifier              |
| `ecad_revision`   | Char      | ECAD revision tracking                    |
| `value`           | Char      | Component Value                           |
| `tolerance`       | Char      | Tolerance (e.g. "10%", +/-0.5pF)          |
| `power_rating`    | Char      | Power in Watts e.g. "10W", "0.25W"        |
| `voltage_rating`  | Char      | Voltage rating in Volts                   |
| `part_type`       | Char      | Part Type (e.g. "Thin Film")              |
---

## 🔒 Data Integrity Rules

The following constraints are enforced at the ORM level:

* `default_code` (Odoo internal part number) **cannot be changed** once lifecycle ≠ Draft
* `plm_pn` **cannot be modified** after lifecycle ≠ Draft
* ECAD mapping fields can be locked after release (configurable)

These rules apply to:

* Manual edits
* Server actions
* Imports

---

## 🔁 Mass Updates (Odoo 18)

This addon is designed to work with **Odoo 18 List View mass actions**.

### Supported

* Action → Update Records
* Server Actions (Python)
* Saved Filters

### Not Supported (by design)

* Direct SQL updates
* Duplicate-and-replace workflows

Example use cases:

* Assign ECAD library to all draft resistors
* Populate missing footprint names
* Update ECAD revision across a family

All updates occur **in place**.

---

## 🧩 ECAD / Fusion 360 Integration Philosophy

This addon does **not** attempt to store:

* Pin mappings
* Gate swaps
* Technology variants

Those remain in the ECAD domain.

Instead, Odoo stores:

* Which **library** to push to
* Which **device/symbol/package names** to reference
* Which **revision** is authoritative

This keeps ERP and ECAD cleanly separated.

---

## 🖥 Views & UI

* Uses standard **List (tree) and Form views**
* Fully compatible with Odoo 18 terminology changes
* No custom JS
* No client-side hacks

Note: Internally, Odoo still uses `tree` views even though the UI calls them *List*.

---

## 🚀 Installation

1. Clone into your custom addons path:

   ```bash
   git clone https://github.com/mikeofpdx/OdoAddons/addons.git engineering_product
   ```

2. Restart Odoo

3. Activate Developer Mode

4. Apps → Update Apps List

5. Install **Engineering Product Extension**

---

## 🧪 Tested With

Untested!

---

## 🧭 Intended Audience

* Hardware startups
* Electronics manufacturers
* Engineering-led organizations
* ERP admins working with ECAD / PLM teams

This module assumes familiarity with:

* Odoo data models
* Engineering part lifecycles
* ECAD library management

---

## 📄 License

MIT License (or replace with your preferred license)

---

## 🤝 Contributions

Contributions are welcome **if they preserve**:

* PLM authority boundaries
* Backward compatibility
* ORM-level validation

Please open an issue before submitting large changes.

---

## 📌 Final Note

This addon is intentionally conservative.

It exists to **prevent silent data corruption** in environments where ERP and PLM must coexist without stepping on each other.

If that describes your organization, this module was written for you.
