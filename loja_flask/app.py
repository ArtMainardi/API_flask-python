from flask import Flask, render_template
from config import listaProdutos

# Cria a aplicação:
app = Flask(__name__)

# Define uma rota:
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/produto")
def produto():
    return render_template("produtos.html", produtos=listaProdutos)

@app.route("/produto/<int:id>")
def buscar_produto(id):
    return render_template("produtos.html", produtos=produto)

@app.route("/categoria/<nome>")
def categoria(nome):
    return render_template("categoria.html")

# Incia o servidor:
if __name__ == "__main__":
    app.run(debug=True)