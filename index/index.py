from myapp import app

@app.route('/index')
def hello():
    return "hello"
