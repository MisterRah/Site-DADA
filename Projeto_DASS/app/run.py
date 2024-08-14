from flask import Flask,render_template, flash
app =  Flask(__name__)
app.secret_key = 'capintaoAmerica'  
@app.route("/")
def inicio():
    flash("Bem-vindo ao nosso site. Aproveite o conteudo" , 'success')
    return render_template("index.html")

@app.route("/quiz")
def quiz():
    flash("Boa Sorte nas perguntas", "success")
    return render_template("quiz.html")
@app.route("/poka")
def poka():
    return render_template("poka.html")
@app.route("/gestao")
def gestao():
    return render_template("gestao.html")
@app.route("/kanban")
def kanban():
    return render_template("kanban.html")
@app.route("/local")
def local():
    return render_template("local.html")
@app.route("/sobre")
def sobre():
    return render_template("sobre.html")
app.run(debug=True)