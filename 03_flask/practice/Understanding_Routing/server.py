from flask import Flask 

app = Flask(__name__)
@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo !"

@app.route('/say/<string:name>')
def say_name(name):
    return f"Hi {name} !"

@app.route('/repeat/<int:num>/<string:item>')
def repeat(num,item):
    return f" {num * item} "

@app.errorhandler(404) 
def invalid_route(e): 
    return "Sorry! No response. Try again."

if __name__ == ("__main__") :
    app.run(debug=True,host="localhost")

