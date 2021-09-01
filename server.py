from os import environ
from flask import Flask
import main

app = Flask(__name__)

@app.route("/")
def home():
    main.tweet_quote()
    return "Anders is tweeting!!"

app.run(host= '0.0.0.0', port=environ.get('PORT'))