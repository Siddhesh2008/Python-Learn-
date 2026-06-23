import requests

base_url="https://pokeapi.co/api/v2/"

def get_pokemon(pokemon_name):
    url=f"{base_url}pokemon/{pokemon_name}"
    response=requests.get(url)
    
    if response.status_code==200:
        return response.json()
    else:
        return "Failed to fetch data"
    
pokemon_name=input("Enter the name of the pokemon: ")
pokemon_data=get_pokemon(pokemon_name)
if pokemon_data:
    print(f"Name: {pokemon_data['name']}")
    print(f"Height: {pokemon_data['height']} ft.")
    print(f"Weight: {pokemon_data['weight']} lbs.")
   