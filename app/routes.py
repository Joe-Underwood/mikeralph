from app import app
from flask import render_template

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('main.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    return render_template('admin.html')

