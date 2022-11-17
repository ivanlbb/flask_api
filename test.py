#aqui se va a enviar una peticion
import requests

BASE = "http://127.0.0.1:7002/"
#BASE = "http://ivan-pb:7002/"

headers = {"Content-Type": "application/json"}

datos = [{'1': '10', '2': '7', '3': '7', '4': '6', '5': '4', '6': '10', '7': '4', '8': '1', '9': '2'}, 
         {'1': '5', '2': '1', '3': '1', '4': '1', '5': '2', '6': '1', '7': '3', '8': '1', '9': '1'},
         {'1': '5', '2': '4', '3': '4', '4': '5', '5': '7', '6': '10', '7': '3', '8': '2', '9': '1'}]


#se le pasa un diccionario y automaticamente lo convierte a form-data
# https://requests.readthedocs.io/en/latest/user/quickstart/#more-complicated-post-requests
payload = {'1': '10', '2': '7', '3': '7', '4': '6', '5': '4', '6': '10', '7': '4', '8': '1', '9': '2'}

# pasar un form-data
r = requests.post(BASE + 'api/predict', data=payload)
print(r.text)

#pasar un json
r = requests.post(BASE + 'api/predict', json=payload)
print(r.text)
