from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)
# app.config.from_object('application.settings')
app.config.from_pyfile('settings.cfg')
# app.config.from_envvar('YOURAPPLICATION_SETTINGS')

# app.secret_key = "my_secret_key"
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "fylesystem"

# app.config.update(
# 		TESTING=True,
#         DEBUG=False,
# 		# TOKEN="ajisdj2j19jdjaj9sd",
# 		SECRET_KEY="a9a9**d7s9asS*D6ˆDˆ678SD("
# )

# print(app.config)
#
# Session(app)

# notes = []

@app.route("/", methods=["GET","POST"])
def index():
    if session.get("notes") is None:
        session["id"] = 1
        # session["num"] = []
        session["notes"] = []

    if request.method == "POST":
        note = request.form.get("note")
        # notes.append(note)
        session["notes"].append("{}-{}".format(str(session["id"]),note))
        session["id"] = session["id"] + 1
        # session["num"].append(session["id"] + 1)
        # notes.append(note)

    return render_template("index.html", notes=session["notes"])
    # return render_template("index.html", notes=notes)

# @app.route("/hello", methods=["GET","POST"])
# def hello():
#     if request.method == "GET":
#         return render_template("index.html")
#     name = request.form.get("name")
#     return render_template("hello.html", name=name)

if __name__ == '__main__':
    # app.debug = True
    # app.run(debug=True)
    # app.config.update(
    # 		TESTING=True,
    #         DEBUG=False,
    # 		# TOKEN="ajisdj2j19jdjaj9sd",
    # 		SECRET_KEY="a9a9**d7s9asS*D6ˆDˆ678SD("
    # )
    # app.secret_key = 'my_secret_key'
    Session(app)
    # print(app.config)
    # print('Secret Key: {}'.format(app.config['SECRET_KEY']))
    # print('Debug: {}'.format(app.config['DEBUG']))
    # print('Test: {}'.format(app.config['TESTING']))
    # print('Flask Env: {}'.format(app.config['FLASK_ENV']))
    # print('Flask Debug: {}'.format(app.config['FLASK_DEBUG']))
    app.run()
