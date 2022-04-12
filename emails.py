from flask import render_template, redirect, request
from flask_app.models.email import User
from flask_app import app

@app.route('/')
def index():
    return render_template("email_index.html")

@app.route('/new_email', methods=['POST'])
def new_email():
    if not User.validate_user(request.form):
        return redirect('/')
    User.save(request.form)
    return redirect('/success')

@app.route('/success')
def success():
    return render_template('goodemail.html', emails = User.show())
