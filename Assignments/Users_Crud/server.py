from flask import Flask, render_template, request, redirect
from user import User

app = Flask(__name__)
app.secret_key = "Chips n dip"

@app.route("/")
def index():
    return redirect("/users")

@app.route("/users")
def users():
    return render_template("users.html",users=User.get_all())

@app.route("/users/edit")


@app.route("/user/new")
def new():
    return render_template("newusers.html")

@app.route("/user/create_user",methods=["POST"])
def create_user():
    print(request.form)
    User.create(request.form)
    return redirect("/users")

@app.route("/delete/<int:id>")
def delete_user():
    data = {
        "id":id
    }
    User.delete.user(data)
    return render_template("/edit.html")

@app.route("/update_user/<int:id>",methods=["POST"])
def update_user():
    data = {
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "emai":request.form["email"],
        "id":id
    }
    User.update.user(data)
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)