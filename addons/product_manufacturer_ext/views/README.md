# Product Manufacturer Search Extension

This is a lightweight extension for the Odoo 18 **OCA Product Manufacturer** module. It enhances the user experience by adding manufacturer-specific search and grouping capabilities to the standard product catalog.

## 🎯 Purpose
While the base `product_manufacturer` module adds essential fields to products, this module extends the **Search View** to allow users to quickly find parts by:
- **Manufacturer Product Code (MPN)**
- **Manufacturer Name** (using "child_of" logic for parent/subsidiary companies)

## ✨ Features
- **Global Search**: Search directly from the top bar using the Manufacturer Product Code.
- **Enhanced Filters**: Adds a "Group By: Manufacturer" option to the search interface.
- **Deep Search**: Locate products by searching for a parent manufacturer company.

## 📋 Requirements
- **Odoo 18.0** (Community or Enterprise)
- **OCA product-attribute**: [product_manufacturer](https://github.com/OCA/product-attribute/tree/18.0/product_manufacturer)

## 🛠 Installation
1. Ensure the OCA `product_manufacturer` module is installed in your Odoo instance.
2. Add this folder to your custom addons path.
3. Update the Apps List in Odoo Developer Mode.
4. Search for `Product Manufacturer Search Extension` and click **Install**.

## 📝 License
This module is licensed under the LGPL-3.0 License.