# Flask Opgaver

Koden i app.py udbyder en række at funtioner gennem [flask](https://flask.palletsprojects.com/en/2.0.x/).
Koden har en række af fejl og mangler som I skal rette.

Start med at læs i Readme.md hvordan I kører koden. Filen er af typen Markdown som ofte bruges til at beskrive hvordan kode skal køres. Den kan læses i råt format(som en .txt fil), men læses bedst i en Markdown reader (fx. [dillinger.io](dillinger.io)).

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






## Noget med POST?
