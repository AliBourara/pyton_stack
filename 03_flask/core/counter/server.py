from flask import Flask,render_template,request,session,redirect

app = Flask(__name__)
app.secret_key = "bazinga"

@app.route('/')
def index():
    if 'visited' in session:
        session["visited"] = session["visited"]+1
    else:
        session["visited"]=0
    return render_template("index.html")

@app.route('/count_process',methods = ["POST"])
def count_process():

    if 'inc_value' in request.form:
        session["inc_value"]=int(request.form['inc_value'])
        new_value = session["visited"]+ int(request.form['inc_value'])
        session["visited"] = new_value
    elif 'inc_value' in session:
        session["visited"] = session["visited"]+session["inc_value"] 
    elif 'visited' in session:
        session["visited"] = session["visited"]+1
    else:
        session["visited"]=0
    return redirect("/count")

@app.route('/count')
def count():
    return render_template("count.html",visited = session["visited"])



@app.route('/clear',methods = ["POST"])
def reset():
    session.clear()
    return redirect("/")


@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug = True)