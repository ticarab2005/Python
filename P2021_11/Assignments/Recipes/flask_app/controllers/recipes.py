from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_bcrypt import bcrypt


@app.route('/new/recipe')
def new_recipe():
    if "user_id" not in session:
        flash("Must be logged in!")
        return redirect('/')
    data = {
        "id":session["user_id"]
    }
    return render_template("new_recipe.html", user=User.get_one_id(data))


@app.route('/create/recipe', methods=["POST"])
def create_recipe():
    if "user_id" not in session:
        flash("Must be logged in!")
        return redirect('/')
    if not Recipe.validate_recipe(request.form):
        return redirect('/new/recipe')
    data = {
        "name":request.form["name"],
        "description":request.form["description"],
        "instructions":request.form["instructions"],
        "date_made":request.form["date_made"],
        "under30":int(request.form["under30"]),
        "user_id":session["user_id"]
    }

    Recipe.save(data)
    return redirect('/dashboard')

@app.route('/update/recipe', methods=["POST"])
def update_recipe():
    if "user_id" not in session:
        flash("Must be logged in!")
        return redirect('/')
    if not Recipe.validate_recipe(request.form):
        return redirect('/new/recipe')
    data = {
        "name":request.form["name"],
        "description":request.form["description"],
        "instructions":request.form["instructions"],
        "under30":int(request.form["under30"]),
        "date_made":request.form["date_made"],
        "id":request.form["id"]
    }
    Recipe.update_recipe(data)
    return redirect('/dashboard')
    

@app.route('/edit/<int:id>')
def edit_recipe(id):
    if "user_id" not in session:
        flash("Must be logged in!")
        return redirect('/')
    data = {
        "id": id
    }
    user_data = {
        "id":session["user_id"]
    }
    return render_template('edit_recipe.html',edit=Recipe.get_one(data), user=User.get_one_id(user_data))


@app.route('/recipe/<int:id>')
def show_recipe(id):
    if "user_id" not in session:
        flash("Must be logged in!")
        return redirect('/')
    data = {
        "id": id
    }
    user_data = {
        "id":session["user_id"]
    }
    return render_template('show_recipe.html', recipe=Recipe.get_one(data), user=User.get_one_id(user_data))


@app.route('/delete/<int:id>')
def delete_recipe(id):
    if "user_id" not in session:
        flash("Must be logged in!")
        return redirect('/')
    data = {
        "id": id
    }
    Recipe.delete_recipe(data)
    return redirect('/dashboard')