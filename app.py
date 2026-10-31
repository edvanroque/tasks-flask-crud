from flask import Flask

app = Flask(__name__)

@app.route("/")
def Olá_Mundo():
  return "Olá, Mundo!"

@app.route("/about")
def about():
  return "Página sobre"

if __name__ == "__main__":
  app.run(debug=True)