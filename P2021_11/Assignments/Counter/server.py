from flask import Flask, render_template,request,redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def index():
    if 'click' in session:
        print('click exists!')
    else:
        print("key 'click' does NOT exist")
    return render_template('index.html')

@app.route('/click',methods=["POST"])
def click():
    temp_num = 0
    session["click"].append(temp_num)
    session.modified = True
    session["total_clicks"] += 1
    request redirect('/')

@app.route("/destroy_session")
def clear():
    session.clear()
    session.pop('reset')
    return redirect("/")

if __name__=='__main__':
    app.run(debug=True)