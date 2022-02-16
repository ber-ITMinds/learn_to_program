# 3. Pokedex API
Koden i app.py udbyder en række af Pokedex funtioner gennem [flask](https://flask.palletsprojects.com/en/2.0.x/).

## Pokedex
Denne Flask API understøtter 3 REST kald:

### GET http://localhost:5000/pokemon?pokemon_no=1

### GET http://localhost:5000/pokemon

### POST http://localhost:5000/pokemon

### DELETE http://localhost:5000/pokemon?pokemon_no=1




## How to run
´set FLASK_DEBUG=1 # Makes the program load any changes to the code instantly.
flask run # Flask will automatically run the python file called *app.py*´

## Pokedex Opgaver


### Udvid informationen der gemmes og oplyses om hver Pokemon
- Type af Pokemon
- Udvikling


### Fire beats grass
Tilføj en funktion der tager 2 pokemon numre og svarer på hvilken der ville have en fordel i en battle baseret på dens type.
Som i "sten, saks, papir".

### Få programmet til at gemme og læse Pokemons til en fil løbende så de ikke slettes hver gang programmet startes på ny.
[Hint](https://www.geeksforgeeks.org/how-to-save-a-python-dictionary-to-a-csv-file/)
