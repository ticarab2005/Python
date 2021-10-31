from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',row=8,col=8,box='red',box1='black')


@app.route('/<int:x>')
def one(x):
    return render_template ('index.html',row=x,col=8,box='red',box1='black')

@app.route('/<int:x>/<int:y>')
def both(x,y):
    return render_template ('index.html',row=x,col=y,box='red',box1='black')

@app.route('/<int:x>/<int:y>/<string:color>')
def colors(x,y,color):
    return render_template('index.html',row=x,col=y,box=color, box1='black')

@app.route('/<int:x>/<int:y>/<string:color>/<string:color1>')
def alternate(x,y,color,color1):
    return render_template('index.html',row=x,col=y,box=color, box1=color1)

if __name__ == "__main__":
    app.run(debug=True)