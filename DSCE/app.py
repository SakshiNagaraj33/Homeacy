from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import hashlib

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def get_db_connection():
    conn = sqlite3.connect('database/users.db')
    conn.row_factory = sqlite3.Row
    return conn

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM user WHERE email = ?', (email,)).fetchone()
        conn.close()
        
        if user and user['password'] == hash_password(password):
            return redirect(url_for('home'))
        else:
            flash('Incorrect email or password')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        hashed_password = hash_password(password)
        
        conn = get_db_connection()
        try:
            conn.execute('INSERT INTO user (email, password) VALUES (?, ?)', (email, hashed_password))
            conn.commit()
        except sqlite3.IntegrityError:
            flash('Email is already registered')
            return render_template('register.html')
        conn.close()
        
        flash('Registration successful, please log in')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
