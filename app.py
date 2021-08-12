#This is the headline, noun, and verb generator microservice for CS_361

# app.py
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/noun', methods=['GET'])
def respond():

    return "Noun"

@app.route('/verb', methods=['GET'])
def post_something():
   def verb_response():

       return "Verb"

@app.route('/', methods=['GET'])
def index():
    horse = "HORSE"
    return horse

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run()