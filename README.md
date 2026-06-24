# E-Commerce Website Using Django

## Overview

The E-Commerce Website is a full-stack web application developed using Django that enables users to browse products, add items to a shopping cart, place orders, and manage their purchases online. The platform provides a secure and user-friendly shopping experience with features such as user authentication, product management, cart functionality, and order processing.

This project demonstrates the implementation of modern web development concepts, database management, and responsive user interfaces using Django.

---

## Features

### User Features

* User Registration and Login
* Secure Authentication System
* Browse Products by Category
* Product Search Functionality
* Product Details Page
* Add to Cart
* Update Cart Quantity
* Remove Items from Cart
* Checkout System
* Order Placement
* Order History
* Responsive Design

### Admin Features

* Admin Dashboard
* Product Management (Add, Update, Delete)
* Category Management
* User Management
* Order Management
* Inventory Tracking

---

## Technology Stack

| Component       | Technology                       |
| --------------- | -------------------------------- |
| Frontend        | HTML, CSS, Bootstrap, JavaScript |
| Backend         | Django (Python)                  |
| Database        | SQLite / MySQL                   |
| Authentication  | Django Authentication System     |
| Styling         | Bootstrap                        |
| Version Control | Git & GitHub                     |
| Web Server      | Django Development Server        |

---

## Project Architecture

```text
User
 │
 ▼
Frontend (HTML, CSS, Bootstrap)
 │
 ▼
Django Views
 │
 ▼
Models
 │
 ▼
SQLite / MySQL Database
```

---

## Project Structure

```text
ecommerce_project/
│
├── ecommerce/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── store/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── manage.py
├── db.sqlite3
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/django-ecommerce.git
cd django-ecommerce
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate Virtual Environment:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Database Migration

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Create Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

---

## Run the Application

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

Admin Panel:

```text
http://127.0.0.1:8000/admin/
```

---

## Database Models

### User

* Username
* Email
* Password

### Product

* Product Name
* Description
* Price
* Image
* Category
* Stock Quantity

### Cart

* User
* Product
* Quantity

### Order

* User
* Order Date
* Total Amount
* Status

---

## Screenshots

### Home Page

Displays featured products and categories.

### Product Page

Shows product details, images, and pricing information.

### Shopping Cart

Allows users to manage selected products before checkout.

### Checkout Page

Collects order details and confirms purchases.

### Admin Dashboard

Enables administrators to manage products, categories, and orders.

---

## Key Functionalities

### Authentication

* User Registration
* User Login
* Logout

### Product Management

* Add Products
* Edit Products
* Delete Products
* Product Search

### Cart Management

* Add to Cart
* Update Quantity
* Remove Product

### Order Processing

* Place Orders
* Order Confirmation
* View Order History

---

## Learning Outcomes

* Django Framework Development
* MVC/MVT Architecture
* Database Design and Management
* User Authentication and Authorization
* CRUD Operations
* Frontend and Backend Integration
* Session and Cart Management
* E-Commerce Application Development

---

## Future Enhancements

* Online Payment Gateway Integration
* Wishlist Functionality
* Product Reviews and Ratings
* Email Notifications
* Invoice Generation
* Discount Coupons
* Order Tracking
* REST API Integration
* Docker Deployment
* Cloud Hosting on AWS

---

## Conclusion

The Django E-Commerce Website provides a complete online shopping solution with product management, user authentication, shopping cart functionality, and order processing. The project demonstrates full-stack web development skills using Django and showcases practical implementation of database management, authentication, and e-commerce workflows.

---

## Author

**Sheela Sankanur**

Python Full Stack Developer | Django Developer
