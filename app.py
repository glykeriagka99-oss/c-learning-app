# Εισαγωγή του Flask και της συνάρτησης για εμφάνιση HTML σελίδων
from flask import Flask, render_template

# Δημιουργία της Flask εφαρμογής
app = Flask(__name__)

# Αρχική σελίδα της εφαρμογής
@app.route("/")
def home():
    return render_template("index.html")

# Σελίδα με το Skill Tree και τα επίπεδα εκμάθησης
@app.route("/skills")
def skills():
    return render_template("skill_tree.html")

# Επίπεδο 1 - Εισαγωγή στη γλώσσα C
@app.route("/lesson/1")
def lesson1():
    return render_template("lesson1.html")

# Επίπεδο 2 - Μεταβλητές στη γλώσσα C
@app.route("/lesson/2")
def lesson2():
    return render_template("lesson2.html")

# Εκκίνηση της εφαρμογής όταν εκτελείται το αρχείο app.py
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)