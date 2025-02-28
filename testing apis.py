import requests
import pandas
import json

def any_pokemon(url):
    response = requests.get(url)
    pokemon_data = response.json()
    pokemon_names = []
    for pokemon in pokemon_data[search]:
        pokemon_names.append(pokemon["name"])
    return pokemon_names
type = "any"

if type == "any":
    url = "https://pokeapi.co/api/v2/pokemon?offset=0&limit=1025"
    search = "results"
    pokemon_names = any_pokemon(url)
else:
    if type == "fire":
        url = f"https://pokeapi.co/api/v2/type/fire"
        search = "pokemon"

    else:
        print("please enter a valid pokemon thoe")
    response = requests.get(url)
    pokemon_data = response.json()

    # Extract the URLs for each Pokémon that has Fire as its type
    pokemon_names = []
    for pokemon in pokemon_data[search]:
        pokemon_names.append(pokemon[search]["name"])


#fire_type_urls = dict.iloc[1,1]


print(pokemon_names[56])
pokemon_name = pokemon_names[56]