from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/cars')
def cars():
    return render_template('cars.html')

@main.route('/europe-delivery')
def europe_delivery():
    return render_template('europe_delivery.html')

@main.route('/user-menu')
@login_required
def user_menu():
    return render_template('user_menu.html', user=current_user)

@main.route('/repair-shop', methods=['GET', 'POST'])
def repair_shop():
    if request.method == 'POST':
        # Process form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        vehicle = request.form.get('vehicle')
        service = request.form.get('service')
        date = request.form.get('date')
        message = request.form.get('message')
        
        # Here you would typically:
        # 1. Save to database
        # 2. Send confirmation email
        # 3. Redirect with success message
        
        flash('Your appointment has been scheduled successfully!', 'success')
        return redirect(url_for('main.repair_shop'))
        
    return render_template('repair_shop.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('main.home'))
        flash('Invalid username or password', 'danger')
    return render_template('login.html')

@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('main.home'))

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'danger')
        else:
            new_user = User(username=username, password=generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            flash('Registered successfully! Please log in.', 'success')
            return redirect(url_for('main.login'))
    return render_template('register.html')