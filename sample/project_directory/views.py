from testapp import app

@app.route('/')
def index():
    return "Hi! kikumura!"