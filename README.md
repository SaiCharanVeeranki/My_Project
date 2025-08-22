# 🍴 MealMate - Online Food Ordering System  

MealMate is a **Django-based web application** that allows users to register as **restaurant owners** or **customers**.  
- **Restaurant Owners** can add, edit, and delete restaurants.  
- **Customers** can browse menus, place orders, and make payments using **Razorpay**.  

---

## 🚀 Features  

### 🔑 Authentication  
- User registration and login (for both **restaurant owners** and **customers**)  
- Secure authentication using Django's built-in system  

### 🏪 Restaurant Management  
- Add new restaurants  
- Edit and update restaurant details  
- Delete restaurants  

### 🍔 Menu & Orders  
- Customers can browse menus  
- Add items to the cart  
- Place orders  

### 💳 Payment Integration  
- **Razorpay** integrated for secure online payments  

---

## 🛠 Tech Stack  
- **Backend**: Django, Python  
- **Frontend**: HTML, CSS, Bootstrap  
- **Database**: SQLite (can be switched to PostgreSQL/MySQL)  
- **Payment Gateway**: Razorpay  

---

## ⚙️ Installation & Setup  

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/mealmate.git
   cd mealmate


## Set Up a Virtual Environment

python -m venv venv
venv\Scripts\activate    # On Windows
source venv/bin/activate # On Mac/Linux


Install Dependencies

pip install -r requirements.txt


Apply Migrations

python manage.py migrate


Create a Superuser

python manage.py createsuperuser


Run the Development Server

python manage.py runserver


Now open your browser at 👉 http://127.0.0.1:8000/
