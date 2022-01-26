from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.survey import User


@app.route('/')
def index():
    return render_template("index.html")

# @app.route('/users', methods=['POST'])
# def create_user():
#     print("Information Collected")
#     print(request.form)
#     return redirect('/')

@app.route('/process_form', methods=['POST'])
def process_form():
        session['sesfirst']=request.form['first_name']
        session['seslast']= request.form['last_name']
        session['seslocal']= request.form['location']
        session['seschar']= request.form['favorite_character']
        session['sestext']= request.form['episode']
        if not User.validate_user(request.form):
            return redirect('/')
        User.create(request.form)
        return render_template('results.html', first= session['sesfirst'], last= session['seslast'],location= session['seslocal'], character= session['seschar'], favorite= session['sestext'])

# @app.route('/result')
# def result():
#     return render_template('results.html', first= session['sesfirst'], last= session['seslast'],location= session['seslocal'], character= session['seschar'], favorite= session['sestext'])
