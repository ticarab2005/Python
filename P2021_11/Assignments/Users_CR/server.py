from flask import Flask, render_template, request, redirect
from users import User

app = Flask(__name__)
app.secret_key = "Chips n dip"

@app.route("/")
def index():
    return redirect("/users")

@app.route("/users")
def users():
    return render_template("users.html",users=User.get_all())

@app.route("/user/new")
def new():
    return render_template("newusers.html")

@app.route("/user/create_user",methods=["POST"])
def create_user():
    print(request.form)
    User.create(request.form)
    return redirect("/users")

if __name__=="__main__":
    app.run(debug=True)