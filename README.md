# 📝 TaskNest – To-Do with Deadlines and Reminders

TaskNest is a modern, mobile-friendly full-stack to-do app built with **Flask**, **MySQL**, and **Tailwind CSS**. It features animated 2.5D card designs, deadline tracking, and responsive UI powered by AOS (Animate On Scroll).

---

## 🚀 Features

- ✅ User Registration & Login (with password hashing)
- 📋 Add, Edit, Delete Tasks
- 📆 Set Deadlines with Countdown
- 📱 Mobile-Responsive Design
- ✨ Beautiful 2.5D UI with AOS animations
- ☁️ Switched from SQLite to MySQL
- 🔐 Secure password storage (Werkzeug)

---

### 📸 Screenshots

## 📸 Screenshots

### 🏠 Home Page  
![Home](task%20home.png)

### 🔐 Login Page  
![Login](task%20login.png)

### 📝 Register Page  
![Register](task%20register.png)

### 📋 Dashboard  
![Dashboard](task%20dashboard.png)

## 🛢️ DB Overview  
![Database](database.png)


---

## 🛠️ Tech Stack

- **Frontend**: HTML5, Tailwind CSS, JavaScript, AOS.js  
- **Backend**: Python Flask  
- **Database**: MySQL (with SQLAlchemy ORM)  
- **Other Tools**: Jinja2, PyMySQL

---

## 📦 Project Structure

tasknest/
├── app.py
├── models.py
├── requirements.txt
├── templates/
│ ├── login.html
│ ├── register.html
│ └── dashboard.html
├── static/
│ ├── style.css
│ └── script.js
├── screenshots/
│ ├── dashboard.png
│ ├── register.png
│ └── mobile.png
└── README.md

yaml
Copy
Edit

---

## 🧪 Local Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/tasknest.git
cd tasknest
2. Create and activate virtual environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # On Windows
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Configure MySQL connection
In app.py, update this:

python
Copy
Edit
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/tasknest'
5. Create database tables
bash
Copy
Edit
python
>>> from app import app
>>> from models import db
>>> with app.app_context():
...     db.create_all()
... 
6. Run the app
bash
Copy
Edit
python app.py
Visit http://127.0.0.1:5000

🌐 Future Improvements
✅ Task categories & tags

🔔 Email or push reminders

📊 Task analytics dashboard

📱 PWA support

📄 License
MIT License © 2025 Sharan S