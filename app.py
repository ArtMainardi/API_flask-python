from Flask import Flask

# Cria a aplicação:
app = Flask(__name__)

# Define uma rota:
@app.route("/")
def index():
    return "Olá mundo! O Flask está funcionando!!"

@app.route("/sobre")
def sobre():
    return '''Esta é a página "sobre"'''

# Incia o servidor:
if __name__ == "__main__":
    app.run(debug=True)