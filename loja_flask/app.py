from flask import Flask, render_template

# Cria a aplicação:
app = Flask(__name__)

# Define uma rota:
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/produto/<int:id>")
def produto(id):
    render_template("produto.html")

@app.route("/categoria/<nome>")
def categoria(nome):
    render_template("categoria.html")

# Incia o servidor:
if __name__ == "__main__":
    app.run(debug=True)