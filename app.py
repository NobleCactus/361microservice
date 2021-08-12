#This is the headline, noun, and verb generator microservice for CS_361

# app.py
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/noun', methods=['GET'])
def respond():

    return "Noun"

@app.route('/post/', methods=['POST'])
def post_something():
    param = request.form.get('name')
    print(param)
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if param:
        return jsonify({
            "Message": f"Welcome {name} to our awesome platform!!",
            # Add this option to distinct the POST request
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "ERROR": "no name found, please send a name."
        })

# A welcome message to test our server
@app.route('/', methods=['GET'])
def index():
    horse = "HORSE"
    return horse

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run()