# Product Datasheets for Odoo 18

A clean, efficient module for managing shared datasheets across multiple products in Odoo. Perfect for electronics distributors, manufacturers, and any business dealing with technical documentation that applies to multiple products.

## 🎯 Problem Solved

In industries like electronics, a single datasheet PDF often applies to hundreds or thousands of product variants. The standard Odoo attachment system would require uploading the same file repeatedly, wasting storage and making updates difficult.

This module introduces a dedicated **Datasheet** model that allows you to:
- Upload a datasheet **once**
- Link it to **unlimited products**
- Update it in **one place**
- Track which products use which datasheets

## ✨ Features

- **Centralized Datasheet Management** - Store datasheets in a dedicated model with proper metadata
- **Many-to-Many Relationships** - Link multiple datasheets to multiple products
- **Smart Buttons** - Quick navigation between products and their datasheets
- **Import/Export Support** - Bulk operations via CSV/Excel
- **Search & Filter** - Find datasheets by manufacturer, part number, or revision
- **Product Count** - See how many products reference each datasheet
- **Revision Tracking** - Track datasheet versions and issue dates
- **External URLs** - Link to manufacturer websites or external repositories

## 📋 Requirements

- Odoo 18.0
- Base `product` module (automatically installed with Odoo)

## 🚀 Installation

### Method 1: Docker (Recommended)

```bash
# Enter your Odoo container
docker exec -it <odoo_container> bash

# Navigate to your custom addons directory
cd /mnt/extra-addons

# Clone the repository
git clone https://github.com/mikeofpdx/OdooAddons.git

# The module will be in: OdooAddons/addons/product_datasheet

# Set proper permissions
chown -R odoo:odoo /mnt/extra-addons/OdooAddons

# Exit and restart container
exit
docker restart <odoo_container>
```

### Method 2: Standard Installation

```bash
# Clone into your Odoo addons directory
cd /path/to/odoo/addons
git clone https://github.com/mikeofpdx/OdooAddons.git

# Restart Odoo server
sudo systemctl restart odoo
```

### Method 3: Direct Module Download

Download just the `product_datasheet` folder from:
```
https://github.com/mikeofpdx/OdooAddons/tree/master/addons/product_datasheet
```

Place it in your Odoo addons directory.

### Activate the Module

1. Go to **Apps** in Odoo
2. Click **Update Apps List** (remove "Apps" filter)
3. Search for "Product Datasheets"
4. Click **Install**

## 📖 Usage

### Creating a Datasheet

1. Navigate to **Inventory → Datasheets**
2. Click **Create**
3. Fill in the details:
   - **Name**: Descriptive name for the datasheet
   - **Manufacturer**: Component manufacturer
   - **Part Number**: Manufacturer's part number
   - **Revision**: Document revision/version
   - **Date Issued**: When the datasheet was published
4. Upload the PDF file
5. Add products in the **Products** tab

### Linking Datasheets to Products

#### From Product View:
1. Open a product
2. Go to the **Datasheets** tab
3. Add existing datasheets or create new ones

#### From Datasheet View:
1. Open a datasheet
2. Go to the **Products** tab
3. Add products that use this datasheet

### Bulk Import

You can import products with datasheet references:

**CSV Format:**
```csv
default_code,name,datasheet_ids/id
RES-001,Resistor 100Ω,__export__.product_datasheet_1
RES-002,Resistor 220Ω,__export__.product_datasheet_1
CAP-001,Capacitor 10µF,__export__.product_datasheet_2
```

**Multiple Datasheets per Product:**
```csv
default_code,name,datasheet_ids/id
IC-001,Microcontroller,__export__.product_datasheet_3,__export__.product_datasheet_4
```

### Bulk Linking via Odoo Shell

For linking one datasheet to many products (e.g., 1000 resistors):

```python
# Access Odoo shell
docker exec -it <container> odoo shell -d <database>

# Find products by pattern
products = env['product.template'].search([
    ('default_code', '=like', 'RES-%')
])

# Get or create datasheet
datasheet = env['product.datasheet'].create({
    'name': 'KOA Speer MF/MFS/RK Series',
    'manufacturer': 'KOA Speer',
    'part_number': 'MF-MFS-RK',
    'datasheet_file': your_base64_pdf,
    'datasheet_filename': 'KOA_MF_Series.pdf',
})

# Link to all products
datasheet.product_ids = [(6, 0, products.ids)]

# Commit
env.cr.commit()
```

## 🗂️ Module Structure

```
product_datasheet/
├── __init__.py
├── __manifest__.py
├── README.md
├── models/
│   ├── __init__.py
│   ├── product_datasheet.py      # Main datasheet model
│   └── product_template.py        # Product extension
├── views/
│   ├── product_datasheet_views.xml
│   └── product_template_views.xml
└── security/
    └── ir.model.access.csv
```

## 🔒 Security

Two access levels are provided:

- **User** (`base.group_user`) - Read-only access to datasheets
- **Manager** (`stock.group_stock_manager`) - Full CRUD access

Modify `security/ir.model.access.csv` to adjust permissions as needed.

## 🎨 Screenshots

### Datasheet List View
View all datasheets with manufacturer, part numbers, and product counts.

### Datasheet Form View
Upload files, add descriptions, track revisions, and link to products.

### Product with Datasheets
Products show linked datasheets in a dedicated tab with smart button access.

## 🛠️ Customization

### Adding Custom Fields

Edit `models/product_datasheet.py` to add fields:

```python
class ProductDatasheet(models.Model):
    _inherit = 'product.datasheet'
    
    your_field = fields.Char(string='Your Field')
```

### Modifying Views

Edit `views/product_datasheet_views.xml` to customize the interface.

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This module is licensed under the LGPL-3.0 License - see the LICENSE file for details.

## 🐛 Bug Reports & Feature Requests

Please use the [GitHub Issues](https://github.com/mikeofpdx/OdooAddons/issues) page to report bugs or request features.

## 📧 Support

- **Documentation**: [Wiki](https://github.com/mikeofpdx/OdooAddons/wiki)
- **Issues**: [GitHub Issues](https://github.com/mikeofpdx/OdooAddons/issues)
- **Repository**: [GitHub](https://github.com/mikeofpdx/OdooAddons)

## 🙏 Credits

Developed for the Odoo community by electronics industry professionals who understand the pain of managing thousands of datasheets.

Created by [mikeofpdx](https://github.com/mikeofpdx)

## 📊 Use Cases

### Electronics Distributors
Link component datasheets to product variants (different package types, tolerances, etc.)

### Manufacturers
Manage technical documentation for product families and assemblies

### Research Labs
Organize equipment specifications and calibration documents

### Automotive
Track part specifications and compliance documents

---

**Made with ❤️ for the Odoo Community**