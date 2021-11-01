from flask import Flask, render_template,request,redirect,session
app = Flask(__name__)
app.secret_key = "Chips n Dip"

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/process",methods=["POST"])
def process():
    print("Here's the form info:")
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comments"] = request.form["comments"]
    return redirect("/results")

@app.route('/results')
def results():
    return render_template("results.html",name=session["name"],location=session["location"],language=session["language"],comments=session["comments"])

@app.route('/Home')
def home():
    session.clear()	
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)