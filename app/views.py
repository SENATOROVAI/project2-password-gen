from flask import render_template, request
from controllers import generate_random_password
from app import app

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', method=['POST'])
def generate_password():
    length =  int(request.form['lenght'])
    password = generate_random_password(length)
    return render_template('index.html', password=password)



