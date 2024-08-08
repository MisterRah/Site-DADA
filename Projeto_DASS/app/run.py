from flask import Flask,render_template
app =  Flask(__name__)
@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/quiz")

def quiz():
    return render_template("quiz.html")

app.run(debug=True)