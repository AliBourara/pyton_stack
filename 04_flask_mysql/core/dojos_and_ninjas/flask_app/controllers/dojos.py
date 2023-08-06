from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    dojos = Dojo.get_all()
    return render_template('index.html', dojos = dojos)

@app.route('/dojo/create', methods=['POST'])
def create():
    Dojo.create_dojo(request.form)
    print('request.form')
    return redirect('/')

@app.route('/dojos/<int:dojo_id>')
def one_dojo(dojo_id):
    dojo = Dojo.get_dojo_by_id({'dojo_id':dojo_id})
    ninjas = Dojo.get_dojos_ninja({'dojo_id':dojo_id})
    return render_template("one_dojo.html", dojo=dojo,ninjas=ninjas)