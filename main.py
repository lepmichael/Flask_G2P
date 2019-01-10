from g2p_en import g2p
import json
from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route('/g2p')
def my_route():
  # page = request.args.get('page', default = 1, type = int)
  word = request.args.get('word', default = '*', type = str)
  phenomes = g2p(word)
  return str(phenomes)

if __name__ == "__main__":
    app.run(debug=True)
