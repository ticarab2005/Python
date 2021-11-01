from flask import Flask, render_template,redirect, session
app = Flask(__name__)
app.secret_key = 'Hakuna Matata'


@app.route('/')
def index():
    if "add" not in session:
        session["add"] = 1
    else:
        session['add'] += 2
    return render_template("index.html")

@app.route('/addition')
def addition():
    session['add'] += 0
    return redirect('/')

@app.route('/destroy_session')
def destroy_session():
    session.clear()	
    return redirect('/')


if __name__=='__main__':
    app.run(debug=True)