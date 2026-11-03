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

# Επίπεδο 2 
@app.route("/lesson/2")
def lesson2():
    return render_template("lesson2.html")
# Επίπεδο 3
@app.route("/lesson/3")
def lesson3():
    return render_template("lesson3.html")
# Επίπεδο 4
@app.route("/lesson/4")
def lesson4():
    return render_template("lesson4.html")
# Επίπεδο 5
@app.route('/lesson/5')
def lesson5():
    return render_template('lesson5.html')
# Επίπεδο 6
@app.route('/lesson/6')
def lesson6():
    return render_template('lesson6.html')

# Επίπεδο 7 
@app.route('/lesson/7')
def lesson7():
    return render_template('lesson7.html')

# Επίπεδο 8 - Συναρτήσεις
@app.route('/lesson/8')
def lesson8():
    return render_template('lesson8.html')
# Εκκίνηση της εφαρμογής όταν εκτελείται το αρχείο app.py
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True,
        use_reloader=False
    )