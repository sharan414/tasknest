from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Task

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Mysql1234@localhost/tasknest_db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        if User.query.filter_by(username=username).first():
            flash('Username already exists')
            return redirect(url_for('register'))
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful. Please log in.')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, request.form['password']):
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        flash('Invalid credentials')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    tasks = Task.query.filter_by(user_id=session['user_id']).order_by(Task.deadline).all()
    return render_template('dashboard.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    if 'user_id' in session:
        title = request.form['title']
        description = request.form['description']
        deadline = datetime.strptime(request.form['deadline'], '%Y-%m-%d')
        priority = request.form['priority']
        task = Task(title=title, description=description, deadline=deadline, priority=priority, user_id=session['user_id'])
        db.session.add(task)
        db.session.commit()
    return redirect(url_for('dashboard'))

@app.route('/complete/<int:id>')
def complete(id):
    task = Task.query.get_or_404(id)
    if task.user_id == session['user_id']:
        task.status = 'Completed'
        db.session.commit()
    return redirect(url_for('dashboard'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('dashboard'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
