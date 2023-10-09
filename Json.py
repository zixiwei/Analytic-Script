import requests
url = 'https://mazeshift-marauders-67598-default-rtdb.firebaseio.com/Player.json'
response = requests.get(url)
data = response.json()
print(data)