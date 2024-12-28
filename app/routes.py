from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def func():
    return render_template('index.html', title='Ecommerce')