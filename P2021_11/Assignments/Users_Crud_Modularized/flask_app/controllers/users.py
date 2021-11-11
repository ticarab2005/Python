from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.user import User


@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    print(User.get_all())
    return render_template("users.html",users=User.get_all())

@app.route('/user/new')
def new():
    return render_template("new_users.html")

@app.route('/user/create_user',methods=["POST"])
def create_user():
    print(request.form)
    User.save(request.form)
    return redirect('/users')

@app.route('/user/edit/<int:id>')
def edit_user(id):
    data = {
        "id":id
    }
    return render_template('edit_user.html',u=User.get_one(data))

@app.route('/user/show/<int:id>')
def show_user(id):
    data = {
        "id":id
    }
    return render_template('show_user.html',u=User.get_one(data))

@app.route('/user/update',methods=["POST"])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/user/delete/<int:id>')
def delete_user(id):
    data = {
        "id":id
    }
    User.delete_user(data)
    return redirect('/users')


