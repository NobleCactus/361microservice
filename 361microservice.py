#This is the headline, noun, and verb generator microservice for CS_361

from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>
    """

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)