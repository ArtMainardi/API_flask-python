from flask import Flask

# Cria a aplicação:
app = Flask(__name__)

# Define uma rota:
@app.route("/")
def index():
    return "Bem vindo à minha loja!!"

@app.route("/sobre")
def sobre():
    return "Essa é uma API criada com Python e Flask para minha loja!"

@app.route("/produtos")
def produtos():
    return '''Lista de produtos:
        \n-> Maçã;
        \n-> Potato;
        \n-> Chinelo Havaianas.
    '''

@app.route("/produto/<int:id>")
def produto(id):
    return f"Produto ID: {id}"

# Incia o servidor:
if __name__ == "__main__":
    app.run(debug=True)