#This is the headline, noun, and verb generator microservice for CS_361

from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)