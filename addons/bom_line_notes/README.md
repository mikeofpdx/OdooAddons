# BOM Line Notes Module for Odoo 18

## Overview
This module adds a "notes" field to individual Bill of Materials (BOM) lines in Odoo 18, allowing users to add additional comments or information for each component in a BOM.

## Features
- **Notes Field**: Adds a text field to each BOM line for storing notes or comments
- **Visible by Default**: The notes field appears in the BOM components list
- **Optional Display**: The field can be shown/hidden using Odoo's optional column feature
- **Change Tracking**: Field changes are tracked in the chatter
- **User-Friendly**: Clean integration with existing BOM views

## Compatibility
- **Odoo Version**: 18.0
- **Dependencies**: `mrp` (Manufacturing) module
- **Tested**: Successfully tested on Odoo 18.0

## Installation

1. Clone or copy the module to your Odoo addons directory:
   ```bash
   cd /path/to/odoo/addons
   git clone <repository-url> bom_line_notes
   # OR
   cp -r bom_line_notes /path/to/odoo/addons/
   ```

2. Set proper permissions:
   ```bash
   chown -R odoo:odoo bom_line_notes
   chmod -R 755 bom_line_notes
   ```

3. Restart Odoo server:
   ```bash
   sudo systemctl restart odoo
   # OR
   ./odoo-bin --stop-after-init
   ```

4. Update the apps list in Odoo:
   - Go to Apps menu
   - Click "Update Apps List"
   - Remove the "Apps" filter to see all modules

5. Search for "BOM Line Notes" and install the module

6. After installation, upgrade the module to ensure database schema is updated:
   ```bash
   ./odoo-bin -u bom_line_notes -d your_database_name
   ```

## Module Structure

```
bom_line_notes/
├── __init__.py                     # Module initialization
├── __manifest__.py                 # Module manifest file
├── models/
│   ├── __init__.py                 # Models initialization
│   └── mrp_bom_line.py            # BOM line model extension
├── views/
│   └── mrp_bom_line_views.xml     # View inheritance and customization
└── README.md                       # This file
```

## Usage

1. Navigate to **Manufacturing > Products > Bill of Materials**
2. Open an existing BOM or create a new one
3. In the **Components** tab, you'll see a "Notes" column after the Product column
4. Click in the notes field to add comments directly in the line
5. The notes will be saved automatically and are visible in all BOM views

### Tips:
- Use notes to document special handling instructions for components
- Add supplier-specific information or part numbers
- Document quality control requirements
- Note any substitutions or alternatives
- The field supports multi-line text for detailed notes

## Technical Details

### Model Extension
The module extends the `mrp.bom.line` model by adding:
- `notes` (Text field): Stores notes for each BOM line
- Field attributes:
  - `string='Notes'`
  - `help='Additional notes or comments for this BOM line'`
  - `tracking=True` - Changes are tracked in chatter

### View Modifications
The module inherits and modifies:
- `mrp.mrp_bom_form_view`: Adds notes field to BOM lines inline tree view
- Field is set to `optional="show"` to be visible by default
- Positioned after the `product_id` field for logical flow

### Database Schema
```sql
-- The module adds this column to mrp_bom_line table:
ALTER TABLE mrp_bom_line ADD COLUMN notes TEXT;
```

## Odoo 18 Compatibility Notes

This module is specifically designed for Odoo 18 and includes:
- Compatible with Odoo 18's Manufacturing module structure
- Uses simplified view inheritance that targets inline BOM line views
- Follows Odoo 18 coding standards and guidelines
- Version specified as `18.0.1.0.0` in manifest
- Tested and verified working on Odoo 18.0

### Known Compatibility Issues:
- **Not compatible with Odoo 17 or earlier**: The BOM view structure changed in Odoo 18
- If upgrading from earlier versions, ensure to test in a staging environment first

## Troubleshooting

### Field not appearing after installation
If the notes field doesn't appear after installation:

1. **Upgrade the module** (most common fix):
   ```bash
   ./odoo-bin -u bom_line_notes -d your_database_name
   ```

2. **Check if field exists in database**:
   ```sql
   SELECT column_name FROM information_schema.columns 
   WHERE table_name = 'mrp_bom_line' AND column_name = 'notes';
   ```

3. **Verify module is properly installed**:
   - Apps > Search "BOM Line Notes" > Should show "Installed"

4. **Clear browser cache** or use incognito mode

5. **Check Odoo logs** for any errors during installation

### Removing old/duplicate modules
If you have an old version of this module:
```sql
DELETE FROM ir_module_module WHERE name LIKE 'bom_line_notes%';
DELETE FROM ir_model_data WHERE module LIKE 'bom_line_notes%';
```
Then restart Odoo and reinstall.

## License
LGPL-3

## Author
Tall Timber IT

## Version History
- **1.0.0** (2025-11-07): Initial release
  - Added notes field to BOM lines
  - Visible by default in BOM component views
  - Change tracking enabled

## Contributing
Contributions are welcome! Please follow these guidelines:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Support
For issues or questions:
- Open an issue on the repository
- Contact your system administrator
- Check Odoo logs for detailed error messages

## Roadmap
Potential future enhancements:
- [ ] Add notes field to BOM reports/PDF exports
- [ ] Make notes field visible in manufacturing orders
- [ ] Add rich text formatting support
- [ ] Export/import notes via CSV