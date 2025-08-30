# Car Rental System 🚗

A web-based Car Rental Management System built with **Django**.  
This project allows **car dealers** to manage vehicles and customers to book cars online.  
It also includes an **admin panel** for superuser management.  

---

## ✨ Features
- User authentication (login/signup)
- Car dealer portal:
  - Manage vehicles (add, update, delete)
  - View customer bookings
- Customer portal:
  - Search available cars
  - Book cars
- Admin panel (Django superuser):
  - Manage all data (dealers, customers, bookings, vehicles)
- Responsive frontend with HTML, CSS, Bootstrap

---

## 🛠 Tech Stack
- **Backend**: Django, Python  
- **Database**: MySQL (or SQLite for local testing)  
- **Frontend**: HTML, CSS, Bootstrap  
- **Version Control**: Git & GitHub  

---

## ⚙️ Installation & Setup

:: 1) Clone and enter the project
git clone https://github.com/benjamind111/Car_Rental_Django.git
cd Car_Rental_Django

:: 2) Create & activate virtual environment
python -m venv venv
call venv\Scripts\activate

:: 3) Install dependencies
pip install -r requirements.txt

:: 4) Create MySQL database (enter your MySQL root password when asked)
mysql -u root -p -e "CREATE DATABASE IF NOT EXISTS car_rental CHARACTER SET utf8mb4;"

:: 5) Make & apply migrations
python manage.py makemigrations
python manage.py migrate

:: 6) Create admin (superuser) for Django admin
python manage.py createsuperuser

:: 7) Run the app
python manage.py runserver

:: Open these in your browser:
:: Home:              http://127.0.0.1:8000/
:: Admin (superuser): http://127.0.0.1:8000/admin/
:: Dealer register:   http://127.0.0.1:8000/car_dealer_portal/register/
:: Dealer login:      http://127.0.0.1:8000/car_dealer_portal/login/
:: Customer login:    http://127.0.0.1:8000/customer_portal/login/
