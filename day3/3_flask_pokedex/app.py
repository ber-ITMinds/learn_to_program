from flask import Flask, request, jsonify
import math

app = Flask(__name__)

db = dict()

@app.route('/')
def welcome():
    return "Welcome to my Flask Pokedex API"


@app.route('/pokemon', methods=['GET', 'POST', 'DELETE'])
def flask_pokemon():

    if request.method == 'GET':
        # send pokemon fra pokedex
        if pokemon_no in db.keys():
            return db[pokemon_no]
        else:
            return "POKEMON NOT FOUND"

        return str(db[pokemon_no])
    elif request.method == 'POST':
        # add pokemon to pokedex
        variables = request.get_json()
        pokemon_no = variables['no']
        pokemon_navn = variables['pokemon']
        if pokemon_no in db.keys():
            return "ALREADY EXISTS"
        else:
            db[pokemon_no] = pokemon_navn
            return "ADDED: \n" + pokemon_navn
    elif request.method == 'DELETE':
        pokemon_no = request.args['pokemon_no']
        # remove pokemon from pokedex
        if pokemon_no in db.keys():
            del db[pokemon_no]
            return "DELETED"
        else:
            return "NOT FOUND"

@app.route('/pokemons', methods=['GET'])
def flask_pokemons():
    return str(list(db.items()))

# Flask setup
if __name__ == '__main__':
    app.run(debug=True)
