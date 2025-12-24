import requests

# The function that fetches data from the API is written outside of main():

def get_pokemon_info(name):
	url = f'https://pokeapi.co/api/v2/pokemon/{name}'
	response = requests.get(url)

# Error handling:

	if response.status_code == 200:
		pokemon_data = response.json()
		return pokemon_data
	else:
		print(f'Failed to retrieve data: {response.status_code}')

# The main() function that contains the main block of code:

def main():

# The script asks the user to enter the name of a Pokemon:

	pokemon_name = input('Enter pokemon name to search: ').lower()
	pokemon_info = get_pokemon_info(pokemon_name)

# The Pokemon's name, ID, height and weight are being printed:

	if pokemon_info:
		print(f'Name: {pokemon_info['name'].capitalize()}')
		print(f'ID: {pokemon_info['id']}')
		print(f'Height: {pokemon_info['height']}')
		print(f'Weight: {pokemon_info['weight']}')

# The main() function can be executed only if the file is run as a script, not imported 
# as a module:

if __name__ == '__main__':
	main()