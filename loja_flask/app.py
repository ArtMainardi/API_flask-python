from flask import Flask

# Cria a aplicação:
app = Flask(__name__)

# Define uma rota:
@app.route("/")
def index():
    return "Olá mundo! O Flask está funcionando!!"

@app.route("/sobre")
def sobre():
    return '''Esta é a página "sobre"'''

@app.route("/produto/<int:id>")
def produto(id):
    return f"Exibindo o produto com o ID {id}"

@app.route("/categoria/<nome>")
def categoria(nome):
    return f"Produtos da categoria: {categoria}"

# Incia o servidor:
if __name__ == "__main__":
    app.run(debug=True)