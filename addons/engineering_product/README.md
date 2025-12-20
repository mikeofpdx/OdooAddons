# Engineering Product Integration
[![Odoo](https://img.shields.io/badge/Odoo-18.0-714B67.svg)](https://www.odoo.com/)
[![License: LGPL-3](https://img.shields.io/badge/License-LGPL--3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0-standalone.html)

This module extends the standard Odoo Product Template with specialized engineering attributes and introduces **ECAD Library Management**. It provides a bridge between ERP inventory and hardware engineering workflows.

## Key Features

### 📚 ECAD Library Management
A centralized repository for organizing components into specific engineering libraries (e.g., "RES-0402", "CAP-CER-0603").
* **Smart Search:** Find libraries instantly by searching for either the descriptive Name or the unique Library Code.
* **One-to-Many Relationship:** Products are assigned to a single library to prevent data fragmentation.
* **🚀 Contextual ECAD Export:** One-click "Export for ECAD" button within the library view generates a pre-formatted CSV containing all linked part data for external system synchronization.

### 🛠️ Enhanced Engineering Attributes
Extends `product.template` with essential technical specifications:
* **ECAD Integration:** Mapping for schematic Symbols and PCB Packages (Footprints).
* **Electrical Specs:** Stored fields for Value, Tolerance, Power Rating, and Voltage Rating.
* **Lifecycle Management:** Tracks part maturity from `Draft` through `Prototype`, `Production`, and `Obsolete`.

### 🔒 Data Integrity & UX
* **Dynamic Read-only States:** Technical specifications are automatically locked for editing once a part moves past the `Draft` stage.
* **Visual Indicators:** Color-coded status decorations (Blue/Green/Red) in list views for instant lifecycle recognition.
* **Optimized Search:** Custom filters to identify "Unassigned" parts and group the catalog by Library or Lifecycle.

## 📋 Data Dictionary

### ECAD Library (`engineering.ecad.library`)
| Field Label | Technical Name | Type | Description |
| :--- | :--- | :--- | :--- |
| **Library Name** | `name` | Char | Descriptive name of the category. |
| **Library Code** | `code` | Char | Short ID used for system sync (e.g., myRES.lbr). |
| **Product Count** | `product_count` | Integer | (Computed) Total parts in this library. |

### Product Template Extensions (`product.template`)
| Field Label | Technical Name | Type | Description |
| :--- | :--- | :--- | :--- |
| **Lifecycle Status** | `lifecycle` | Selection | Draft, Prototype, Production, or Obsolete. |
| **ECAD Device** | `ecad_symbol` | Char | Schematic symbol name. |
| **ECAD Package** | `ecad_package` | Char | PCB footprint/package name. |
| **Value/Specs** | `value`, `tolerance`, `part_type`, `voltage_rating`, `power_rating`| Char | Component-specific technical data. |
| **Library Assigned** | `ecad_library_assigned` | Boolean | (Stored) Indexed for fast filtering. |

## Technical Specifications

### Dependencies
* `product`: Extends `product.template`

### UI & UX Logic
* **Form View:** Adds an "Engineering" tab with conditional visibility and lifecycle-based `readonly` constraints.
* **Search View:** Adds "Unassigned to Library" and "Draft Lifecycle" filters + "Group By" options.
* **Export Logic:** Python-based CSV generation using `io.StringIO` and `base64` for seamless browser downloads.

## Installation

1. Clone this repository into your Odoo `addons` folder:
   ```bash
   git clone [https://github.com/mikeofpdx/OdooAddons.git](https://github.com/mikeofpdx/OdooAddons.git)
2. Update your Odoo configuration to include the addons/engineering_product path.
3. Update your App List in the Odoo UI (Debug Mode required).
4. Install Engineering Product Integration.
