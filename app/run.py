from flask import Flask,render_template, flash
app =  Flask(__name__)
app.secret_key = 'capintaoAmerica'  
@app.route("/")
def inicio():
    flash("Bem-vindo ao nosso site. Aproveite o conteudo" , 'success')
    return render_template("index.html")

@app.route("/quiz")
def quiz():
    flash("Boa Sorte nas perguntas, acha que consegue acertar todas?", "success")
    return render_template("quiz.html")

@app.route("/poka")
def poka():
    flash("Conheça um pouco sobre Poka Yoke, com Kevyn Levi", "success")
    return render_template("poka.html")

@app.route("/gestao")
def gestao():
    flash("Conheça um pouco sobre Gestão Visual, com Kaila Ferraz", "success")
    return render_template("gestao.html")

@app.route("/kanban")
def kanban():
    flash("Conheça um pouco sobre Kanban, com Tayane", "success")
    return render_template("kanban.html")

@app.route("/local")
def local():
    flash("Conheça um pouco sobre um Local De Trabalho Autoexplicativo, com Gabriel", "success")
    return render_template("local.html")

@app.route("/sobre")
def sobre():
    flash("Conheça um pouco sobre cada um dos membros do grupo", "success")
    return render_template("sobre.html")

@app.route("/documentos")
def documentos():
    flash("Saiba como o site foi feito", "success")
    return render_template("documentos.html")

app.run(debug=True)