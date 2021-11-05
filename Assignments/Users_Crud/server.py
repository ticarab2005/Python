from flask import Flask, render_template, request, redirect
from user import User

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template("users.html",users=User.get_all())

@app.route('/user/new')
def new():
    return render_template("newusers.html")

@app.route('/user/create_user',methods=["POST"])
def create_user():
    print(request.form)
    User.save(request.form)
    return redirect('/users')

@app.route('/user/edit/<int:id>')
def edit(id):
    data = {
        "id":id
    }
    return render_template('edit_user.html',user=User.get_one(data))


@app.route('/user/show/<int:id>')
def show(id):
    data = {
        "id":id
    }
    user = User.get_one(data)
    return redirect("show_user.html",user=user)

@app.route('/user/update',methods=["POST"])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/user/delete/<int:id>')
def delete(id):
    data = {
        "id":id
    }
    User.delete(data)
    return redirect('/users')

if __name__=="__main__":
    app.run(debug=True)