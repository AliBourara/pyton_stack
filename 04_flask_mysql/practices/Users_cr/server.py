from flask import Flask,render_template,redirect,request
from user import User

app = Flask (__name__)

@app.route("/")
def index():
    users = User.get_all()
    return render_template("index.html",users = users)

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/new_create",methods=['POST'])
def create():
    data={
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"],
    }
    User.save(data)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)