from flask import Flask


app = Flask("__name__")

@app.route("/")
def index():
    return "Salom Backend Dasturchi"

@app.route("/about")
def about():
    return "about page"


if __name__ == "__main__":
    app.run(debug=True)
