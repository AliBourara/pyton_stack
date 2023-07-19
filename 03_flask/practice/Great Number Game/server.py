from flask import Flask ,render_template,redirect,session,request

app = Flask(__name__)
app.secret_key = "for the horde"

@app.route("/")
def index():
    import random
    session["rng"] = random.randint(1, 100)
    print(session['rng'])
    session['attempts'] = 5
    return render_template("index.html")

@app.route('/guess_proccess' , methods = ["POST"])
def guess_proccess():
    session["guess_value"] = int(request.form["guess_value"])
    if "guess_value" in session:
        session['attempts'] -=1 
    else :
        session['attempts'] = 0
    return redirect("/guess",)
@app.route('/leaderboard' , methods = ["POST"])
def leaderboard():
    session["save"] = request.form['save']
    session['score'] = 5 - session["attempts"]
    return render_template("leaderboard.html")

@app.route('/guess')
def guess(): 
    print(session["guess_value"])
    print(session['rng'])
    print(session["attempts"])
    return render_template("guess.html")

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')



if __name__ == "__main__" :
    app.run(debug=True)