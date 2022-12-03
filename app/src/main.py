from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('index.html', name=name)

@app.route("/example")
def hello_world():
    return "<p>Hello, World!</p>"