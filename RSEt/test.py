import requests
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='apijson'
res = requests.get(BASE_URL+ENDPOINT)
data=res.json()
print(data)
