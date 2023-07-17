from flask import Flask, render_template, request
from controllers import generate_random_password

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('app\static\index.html')

@app.route('/generate', method=['POST'])
def generate_password():
    length =  int(request.form['lenght'])
    password = generate_random_password(length)
    return render_template('app\static\index.html', password=password)



