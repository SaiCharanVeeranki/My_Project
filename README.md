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

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv venv  
   venv\Scripts\activate    # On Windows  
   source venv/bin/activate # On Mac/Linux  


3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt



4. **Apply Migrations**
   ```bash
   python manage.py migrate


5. **Create a Superuser**
   ```bash
   python manage.py createsuperuser


6. **Run the Development Server**
   ```bash
   python manage.py runserver

***Now open your browser at 👉 http://127.0.0.1:8000/***



***📂 Project Structure***
MealMate/
│── MealMate/
│   │── __pycache__/
│   │── __init__.py
│   │── asgi.py
│   │── settings.py
│   │── urls.py
│   │── wsgi.py
│
│── delivery/
│   │── __pycache__/
│   │── migrations/
│   │── static/delivery/css/
│   │── templates/delivery/
│   │   ├── Failed.html
│   │   ├── add_res.html
│   │   ├── base.html
│   │   ├── checkout.html
│   │   ├── cusdisplay_res.html
│   │   ├── cusmenu.html
│   │   ├── display_res.html
│   │   ├── index.html
│   │   ├── menu.html
│   │   ├── menu_form.html
│   │   ├── orders.html
│   │   ├── show_cart.html
│   │   ├── sign_in.html
│   │   ├── sign_up.html
│   │   ├── success.html
│   │   ├── update_res.html
│   │   ├── userdata.html
│   │── __init__.py
│   │── admin.py
│   │── apps.py
│   │── forms.py
│   │── models.py
│   │── tests.py
│   │── urls.py
│   │── views.py
│
│── db.sqlite3
│── manage.py
│── requirements.txt



***📌 Key Learnings***

- Gained hands-on experience with Django Framework and MVC architecture

- Implemented role-based authentication for multiple user types

- Integrated Razorpay payment gateway for real-world transaction handling

- Strengthened skills in HTML, CSS, Bootstrap, and Django templates

- Learned how to design a full-stack CRUD application and deploy locally
