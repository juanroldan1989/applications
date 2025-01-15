from flask import Flask, jsonify
import random

app = Flask(__name__)

farewells = ["See ya later", "Peace out", "Adios",
             "Ciao", "Sayonara", "Hasta la vista",
             "Auf Wiedersehen", "Arrivederci", "Chow",
             "Ta-ta", "Cheerio"]

@app.route('/phrase', methods=['GET'])
def get_phrase():
  return jsonify(phrase=random.choice(farewells))

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5004)
