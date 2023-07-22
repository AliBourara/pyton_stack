from flask import Flask,render_template,request,redirect,session

app = Flask(__name__)
app.secret_key = "there is no spoon"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods = ["POST"])  
def process():
    session["fav_lang"]=request.form.getlist('fav_lang')
    session['name']= request.form['name']
    session["grade"] = request.form['grade']
    session["location"]= request.form["location"]
    session["comments"]= request.form["comments"]
    return redirect ("/result")

@app.route("/result")
def result():
    return render_template("result.html")

@app.route('/clear')
def reset():
    session.clear()
    return redirect("/")

if __name__ == "__main__" :
    app.run(debug=True)