from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/skills")
def skills():
    return render_template("skill_tree.html")


@app.route("/lesson/1")
def lesson1():
    return render_template("lesson1.html")

@app.route("/lesson/2")
def lesson2():
    return render_template("lesson2.html")


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)