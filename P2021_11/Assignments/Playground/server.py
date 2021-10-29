from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def level1():
    return render_template("index.html",num=3,color="aqua")

@app.route('/play/<int:number>')
def level2(number):
    return render_template("index.html",number, color="aqua")

if __name__=="__main__":
    app.run(debug=True)
