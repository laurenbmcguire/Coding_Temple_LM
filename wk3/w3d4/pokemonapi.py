from http.client import responses
import requests

url = 'https://pokeapi.co/docs/v2/pokemon/?limit=3'
#no api key needed but if you do use one use something like
#api_key = ''

# api_call = f"{base_url}?q={'charateristics'}"


print(url)

response = requests.get(url)

# dir(response)

print(response.status_code)

# response.url="https://pokeapi.co/docs/v2#characteristics"

response.json

print(response)
   