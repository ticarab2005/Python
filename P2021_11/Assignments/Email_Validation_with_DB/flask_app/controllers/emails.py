from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.email import Email

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validate',methods=["POST"])
def validate():
    if Email.validate_email(request.form):
        Email.save(request.form)
        return redirect("/success")
    return redirect("/")

@app.route('/success')
def results():
    return render_template("/success.html", emails = Email.get_all_email())

@app.route('/email/delete/<int:id>')
def delete_email(id):
    data = {
        "id":id
    }
    Email.delete_email(data)
    return redirect('/')
