from flask import Flask, g ,request

app = Flask(__name__)
app.debug = True

@app.route('/')
def hello():
    return "hello"
