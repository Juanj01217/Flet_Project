import urllib.request
import json
import features.pokemonEntity as pkEntity

def get_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    try:
        with urllib.request.urlopen(url) as response:
            if response.code == 200:
                data = json.loads(response.read())
                name = data['name']
                type_ = data['types'][0]['type']['name']
                image_url = data['sprites']['front_default']
                level = 1
                pokemon = pkEntity.pokemonEntity(name, type_, level, image_url)
                return pokemon
            else:
                print("Pokemon not found!")
                return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_pokemon_list(limit=100):
    url = f"https://pokeapi.co/api/v2/pokemon?limit={limit}"
    try:
        with urllib.request.urlopen(url) as response:
            if response.code == 200:
                data = json.loads(response.read())
                pokemon_names = [item['name'] for item in data['results']]
                return pokemon_names
            else:
                print("Failed to retrieve Pokemon list!")
                return []
    except Exception as e:
        print(f"Error: {e}")
        return []
    else:
        print("Failed to retrieve Pokemon list!")
        return []