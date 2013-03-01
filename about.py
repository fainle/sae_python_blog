from flask import Flask, g ,request

app2 = Flask(__name__)
app2.debug = True

@app2.route('/about')
def hello():
    return "hello about"
