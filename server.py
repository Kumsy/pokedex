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
# Pokemon info is accessed by a pokemon's number. Ex: bulbasaur == 1
url = 'https://pokeapi.co/api/v2/pokemon/1/'
pokemon_api = requests.get(url)

# Front pokemon sprite image url
pprint(pokemon_api.json()['sprites']['front_default'])

# Pokemon name
pprint(pokemon_api.json()['name'])


# Pokemon types (fire, water, grass, etc)
pokemon_types = pokemon_api.json()['types']
for types in pokemon_types:
    pprint(types['type']['name'])





###########################
if __name__ == "__main__":
    app.debug = True


    app.run(host="0.0.0.0")