from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return"Hello,Flask!"
if __name__ == '__main__':
    app.run(debug=True)
    from flask import Flask, render_template

    app = Flask(__name__)


    @app.route('/')
    def index():
        return "Index!"


    @app.route('/Hello')
    def hello():
        return "Hello, World!"


    @app.route("/members")
    def members():
        return "Members"


    @app.route("/members/<name>/")
    def getMember(name):
        return name


    if __name__ == '__main__':
        app.run(debug=True)