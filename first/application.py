from flask import Flask

app = Flask(__name__)

@app.route("/<string:name>")
def index(name):
    name = str.capitalize(name)
    return f"<h1>Hello, {name}</h1>"

if __name__ == '__main__':
    app.run()
