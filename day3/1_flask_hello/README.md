# 1. Flask Hello ___
Se [FLASK.md](FLASK.md) for information om hvordan flask køres.

## How to run
´set FLASK_DEBUG=1 # Makes the program load any changes to the code instantly.
flask run # Flask will automatically run the python file called *app.py*´

# Flask Opgaver
Koden i app.py udbyder en række at funtioner gennem [flask](https://flask.palletsprojects.com/en/2.0.x/).
Koden har en række af fejl og mangler som I skal rette.

## Hello World!
Det første endpoint siger hej til en bruger som bliver givet igennem variablerne _firstname_ og _lastname_.
[http://127.0.0.1:5000/hello?firstname=guido&lastname=rossum](http://127.0.0.1:5000/hello?firstname=guido&lastname=rossum)

### Få navnet til at være i 2 ord og med stort forbogstav
Få programmet til at svare "Hello Guido Rossum" på http://127.0.0.1:5000/hello?firstname=guido&lastname=rossum

### Intet navn
Få programmet til at svare noget passende når et navn ikke er inkluderet [http://127.0.0.1:5000/hello](http://127.0.0.1:5000/hello)

### Kun fornavn
I nedenstående kald har personen kun et fornavn. Få koden til at acceptere dette
[http://127.0.0.1:5000/hello?firstname=Yoda](http://127.0.0.1:5000/hello?firstname=Yoda)

### Mulighed for mellemnavn
Få programmet til at håndtere et eventuelt mellemnavn.




### Noget med POST?
