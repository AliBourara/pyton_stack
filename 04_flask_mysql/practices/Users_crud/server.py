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

@app.route('/user/edit/<int:id>')
def edit(id):
    one_user = User.get_one({"id":id})
    return render_template("edit_user.html", user = one_user)

@app.route('/user/<int:id>')
def show(id):
    one_user = User.get_one({"id":id})
    return render_template("one_user.html", user = one_user)

@app.route("/user/<int:id>/update",methods = ['POST'])
def update_user(id):
    data = {
        **request.form,
        'id':id
    }
    User.update(data)
    return redirect('/')

@app.route('/user/<int:id>/destroy', methods=['POST'])
def destroy(id):
    User.destroy({'id':id})
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)