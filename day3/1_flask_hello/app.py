from flask import Flask, request, jsonify
app = Flask(__name__)

def send_hello(who):
    return "Hello " + who

@app.route('/')
def welcome():
    return "Welcome to my Flask API"

# localhost:5000/hello?firstname=benjamin&lastname=eriksen
@app.route('/hello', methods=['GET'])
def hello():
    firstname = request.args.get('firstname', type = str)
    lastname = request.args.get('lastname', type = str)
    return send_hello(firstname+lastname)


# Flask setup
if __name__ == '__main__':
    app.run(debug=True)
