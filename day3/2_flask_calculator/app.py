from flask import Flask, request, jsonify
import math

app = Flask(__name__)

# Indsæt add, minus, multiply, division her

def add(a,b):
    # jeres kode her
    return a + b

def minus(a,b):
    # jeres kode her
    return

def multiply(a,b):
    # jeres kode her
    return

def division(a,b):
    # jeres kode her
    return

@app.route('/')
def welcome():
    return "Welcome to my Flask Calculator API"

# localhost:5000/hello?firstname=benjamin&lastname=eriksen
@app.route('/add', methods=['GET'])
def flask_add():
    variables = request.get_json()
    a = variables['a']
    b = variables['b']
    return str(add(a,b))

# indsæt flask minus, multiply, division funktioner her

@app.route('/pi', methods=['GET'])
def flask_pi():
    return str(math.pi)

# Flask setup
if __name__ == '__main__':
    app.run(debug=True)
