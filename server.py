from flask import Flask, render_template
from jinja2 import StrictUndefined
from pprint import pprint
import requests, json

app = Flask(__name__)

# Flask Sessions and Debug Toolbar
app.secret_key = 'omnislash'
app.jinja_env.undefined = StrictUndefined

# Routes
@app.route('/')
def home():
    return 'work in progress'

# Test calls
url = 'https://pokeapi.co/api/v2/pokemon/'
pokemon_api = requests.get(url)
pprint(pokemon_api.json())




###########################
if __name__ == "__main__":
    app.debug = True


    app.run(host="0.0.0.0")