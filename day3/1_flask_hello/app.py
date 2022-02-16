from flask import Flask, request, jsonify
app = Flask(__name__)

def send_hello(who):
    return "<h1> Hello " + who + "</h1>"

@app.route('/')
def welcome():
    return """
    <h1 style='color: red;'>I'm a red H1 heading!</h1>
    <p>This is a lovely little {}</p>
    <code>Flask is <em>awesome</em></code>
    """.format("paragraph")

# localhost:5000/hello?firstname=benjamin&lastname=eriksen
@app.route('/hello', methods=['GET'])
def hello():
    firstname = request.args.get('firstname', type = str)
    lastname = request.args.get('lastname', type = str)
    return send_hello(firstname+lastname)


# Flask setup
if __name__ == '__main__':
    app.run(debug=True)
