from flask import Flask, g ,request

app = Flask(__name__)
app.debug = True

@app.route('/index')
def hello():
    return "hello"
