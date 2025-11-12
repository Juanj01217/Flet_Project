import requests
import features.pokemonEntity as pkEntity

def get_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        name = data['name']
        type_ = data['types'][0]['type']['name']
        image_url = data['sprites']['front_default']
        level = 1  # Default starting level
        pokemon = pkEntity.pokemonEntity(name, type_, level, image_url)
        return pokemon
    else:
        print("Pokemon not found!")
        return None

def get_pokemon_list(limit=100):
    url = f"https://pokeapi.co/api/v2/pokemon?limit={limit}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        pokemon_names = [item['name'] for item in data['results']]
        return pokemon_names
    else:
        print("Failed to retrieve Pokemon list!")
        return []