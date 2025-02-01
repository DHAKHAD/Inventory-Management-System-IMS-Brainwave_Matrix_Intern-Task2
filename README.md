# Inventory Management System (IMS)

Overview

The Inventory Management System (IMS) is a Python-based desktop application that helps manage inventory operations such as employee management, supplier records, product categories, sales tracking, and billing. The application features a user-friendly Tkinter GUI and uses SQLite as the database backend.

Features

User-Friendly GUI: Built using Tkinter.

Dashboard Overview: Displays total Employees, Suppliers, Categories, Products, and Sales.

Navigation Menu: Access different sections like Employee, Supplier, Category, Product, Sales, and Billing.

Database Management: Uses SQLite3 to store and retrieve inventory data.

Live Clock: Displays real-time date and time.

Logout Functionality: Secure exit from the system.

Technologies Used

Python 3

Tkinter (GUI Library)

SQLite3 (Database)

PIL (Python Imaging Library)

OS Module (File Handling)

Time Module (Real-time Clock)

Installation

Clone the repository:

git clone https://github.com/DHAKHAD/Inventory-Management-System-IMS-Brainwave_Matrix_Intern-Task2
cd inventory-management-system

Install dependencies:

pip install -python3 --version


Run the application:

python dashboard.py

Folder Structure

project-root/
│-- img/                # Contains images for the GUI
│-- SQL Database/       # Contains SQLite database file (IMS.db)
│-- Supplier.py         # Supplier Management Module
│-- billing.py          # Billing Module
│-- category.py         # Category Management Module
│-- employee.py         # Employee Management Module
│-- product.py          # Product Management Module
│-- sales.py            # Sales Management Module
│-- dashboard.py        # Main Application Script
│-- login.py            # Login System
│-- README.md           # Documentation

Usage

Start the application: Run python main.py.

Login and navigate using the left menu.

Manage Employees, Suppliers, Products, and Sales via respective sections.

Track total counts of inventory items from the dashboard.

Logout securely when done.

Future Enhancements

Implement user authentication.

Add exporting reports in CSV or PDF format.

Introduce barcode scanning for product management.

Enhance the UI design for a better user experience.

Developed By

Sunil Nagar
