import requests
BASE='http://127.0.0.1:3400/'
r = requests.get(BASE + "/api/v1/helloWorld")

assert r.json()['message'] == 'hello world'
