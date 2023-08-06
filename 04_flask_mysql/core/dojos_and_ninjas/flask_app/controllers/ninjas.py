from flask import render_template, redirect, session, request
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def new_ninja():
    dojos = Dojo.get_all()
    return render_template('new_ninja.html', dojos = dojos)

@app.route('/ninjas/add', methods=['POST'])
def add_ninja():
    print(request.form)
    Ninja.create_ninja(request.form)
    return redirect('/')