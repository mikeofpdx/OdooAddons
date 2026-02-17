# Product Tariff Management

![Odoo Version](https://img.shields.io/badge/Odoo-18.0-714B67.svg)
![License](https://img.shields.io/badge/License-LGPL--3-blue.svg)
![Version](https://img.shields.io/badge/Version-18.0.0.0-green.svg)

## Overview
This module extends **Odoo 18** to manage international trade compliance and automated cost calculations. It adds **HS Tariff Codes** and **Tariff Rates** to products and ensures these costs are reflected in the procurement workflow.

Unlike standard Odoo, this module calculates a dedicated **Tariff Bill** on Purchase Orders, providing visibility into landed costs before the items even arrive.

---

## ✨ Key Features

* **Product Master Data Extension:**
    * Adds `HS Tariff Code` (String) for customs documentation.
    * Adds `Tariff Rate (%)` (Float) to define the duty percentage per product.
* **Purchase Order Integration:**
    * Automatically maps the Tariff Rate from the Product to the **Purchase Order Line**.
    * Adds a dedicated **Tariff Charges** line in the Order Total summary.
* **Automated Calculations:**
    * The `Total` amount of the Purchase Order automatically includes the calculated Tariff Charges ($Subtotal \times Rate$).
* **Reporting Ready:**
    * The **RFQ** and **Purchase Order** PDF reports are extended to show the Tariff % per line and the total Tariff Charges in the footer.

---

## 🛠 Installation

1.  Download or clone this repository into your Odoo `addons` folder.
2.  Restart your Odoo Server.
3.  Log in as an Administrator and activate **Developer Mode**.
4.  Navigate to the **Apps** menu and click **Update Apps List**.
5.  Search for `Product Tariff Management` and click **Activate**.

---

## 📖 How It Works

### 1. Set the Tariff on the Product
Open any product and navigate to the **General Information** tab. You will see two new fields under the Barcode section:
* **HS Tariff Code:** e.g., `8517.12.00`
* **Tariff Rate (%):** e.g., `15.0`

### 2. Create a Purchase Order
When you select a product on an RFQ/PO, the rate is fetched automatically. 
* The **Tariff Charges** are calculated dynamically as you add items.
* The **Total** at the bottom of the screen will update to: 
    $$Untaxed + Taxes + Tariff Charges = Total$$

---

## 📁 Technical Structure

```text
product_tariff_management/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── product_template.py
│   └── purchase_order.py
├── views/
│   ├── product_views.xml
│   └── report_purchase_quotation.xml
└── README.md