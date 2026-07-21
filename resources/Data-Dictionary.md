# 📚 LakeMart Retail Corporation - Data Dictionary

Welcome to the official Data Dictionary for the **60 Days PySpark & Spark SQL Challenge**.

This document explains every dataset used throughout the challenge.

---

# Business Domain

**Industry:** Retail & E-Commerce

**Company:** LakeMart Retail Corporation

The datasets simulate a real-world retail company with customers, products, stores, orders, inventory, and payments.

---

# Database Overview

| Table | Type | Records |
|---------|------|---------:|
| customers | Dimension | 2,000 |
| products | Dimension | 500 |
| stores | Dimension | 50 |
| orders | Fact | 15,000 |
| order_items | Fact | 25,000 |
| payments | Fact | 5,000 |
| inventory | Fact | 2,500 |

Total Records ≈ **50,000**

---

# Entity Relationship

customers
      │
      ▼
   orders ─────────► payments
      │
      ▼
 order_items
      │
      ▼
  products
      ▲
      │
 inventory
      ▲
      │
   stores

---

# customers.csv

Purpose

Contains customer information.

| Column | Type | Description |
|---------|------|-------------|
| customer_id | INT | Primary Key |
| first_name | STRING | Customer First Name |
| last_name | STRING | Customer Last Name |
| gender | STRING | Gender |
| email | STRING | Email Address |
| phone | STRING | Mobile Number |
| date_of_birth | DATE | Birth Date |
| city | STRING | City |
| state | STRING | State |
| country | STRING | Country |
| postal_code | STRING | Postal Code |
| join_date | DATE | Registration Date |
| loyalty_status | STRING | Bronze / Silver / Gold / Platinum |

Primary Key

customer_id

---

# products.csv

Purpose

Contains product master data.

| Column | Type |
|---------|------|
| product_id | INT |
| product_name | STRING |
| category | STRING |
| brand | STRING |
| supplier | STRING |
| unit_price | DECIMAL |
| cost_price | DECIMAL |
| stock_unit | STRING |
| launch_date | DATE |
| active | BOOLEAN |

Primary Key

product_id

---

# stores.csv

Purpose

Contains store information.

| Column | Type |
|---------|------|
| store_id | INT |
| store_name | STRING |
| city | STRING |
| state | STRING |
| region | STRING |
| manager_name | STRING |
| opening_date | DATE |

Primary Key

store_id

---

# orders.csv

Purpose

Contains customer orders.

| Column | Type |
|---------|------|
| order_id | INT |
| customer_id | INT |
| store_id | INT |
| order_date | DATE |
| delivery_date | DATE |
| order_status | STRING |
| total_amount | DECIMAL |
| discount | DECIMAL |
| tax | DECIMAL |

Primary Key

order_id

Foreign Keys

customer_id → customers

store_id → stores

---

# order_items.csv

Purpose

Contains every product purchased in an order.

| Column | Type |
|---------|------|
| order_item_id | INT |
| order_id | INT |
| product_id | INT |
| quantity | INT |
| unit_price | DECIMAL |
| discount | DECIMAL |

Primary Key

order_item_id

Foreign Keys

order_id → orders

product_id → products

---

# payments.csv

Purpose

Contains payment information.

| Column | Type |
|---------|------|
| payment_id | INT |
| order_id | INT |
| payment_method | STRING |
| payment_status | STRING |
| payment_date | DATE |
| payment_amount | DECIMAL |

Primary Key

payment_id

Foreign Key

order_id → orders

---

# inventory.csv

Purpose

Contains product inventory.

| Column | Type |
|---------|------|
| inventory_id | INT |
| store_id | INT |
| product_id | INT |
| quantity_available | INT |
| reorder_level | INT |
| last_updated | DATE |

Primary Key

inventory_id

Foreign Keys

store_id → stores

product_id → products

---

# Intentional Data Quality Issues

This dataset intentionally contains dirty data to simulate production systems.

Examples include

- Extra spaces
- Uppercase and lowercase inconsistencies
- Missing values
- Invalid emails
- Different phone number formats
- Multiple date formats
- Currency symbols
- Duplicate records
- Typographical errors
- NULL values
- Blank strings
- Unknown values

Students will clean these datasets throughout the challenge using **PySpark** and **Spark SQL**.

---

# Learning Goal

By the end of this challenge, students will transform raw retail data into production-ready datasets using modern Data Engineering practices.
