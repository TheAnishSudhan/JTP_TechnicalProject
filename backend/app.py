from flask import Flask, jsonify, request, render_template, abort
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*',"allow_headers": "Access-Control-Allow-Origin, Authorization, Access-Control-Allow-Headers, Content-Type, Origin, Accept, X-Requested-With, Access-Control-Allow-Methods, Allow"}})
CORS(app, resources={r"/*":{'origins':'http://localhost:5173/ping', "allow_headers": "Access-Control-Allow-Origin, Authorization, Access-Control-Allow-Headers, Content-Type, Origin, Accept, X-Requested-With, Access-Control-Allow-Methods, Allow"}})

api_key = '2b904b89a0694e89b4aae3704f28c5df'; 

places = []

import requests
from requests.structures import CaseInsensitiveDict

@app.route('/ping', methods=['POST'])
def ping_pong():
    data = request.get_json()
    destination = data.get('destination')
    category = data.get('category')
    limit=data.get('limit')

    api_place_url="https://api.geoapify.com/v1/geocode/search?text="

    place_params = {
        'text': destination,
        'apiKey': api_key
    }

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    place_resp = requests.get(api_place_url, params=place_params, headers=headers)
    place_data = place_resp.json()
    place_id = place_data['results'][0]['place_id']
    

    api_url = "https://api.geoapify.com/v2/places?categories="
    types_params = {
        'categories' : category,
        'place' : place_id,
        'limit' : limit,
        'apiKey' : api_key
    }

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    types_resp = requests.get(api_url, params=types_params, headers=headers)
    types_data = types_resp.json()
    types_locations = types_data['features']

    places = []
    for location in types_locations:
         places.append({
            'name': location['properties']['name'],
            'address': location['properties']['formatted'],
        })

    # return jsonify({'message': 'Form data received successfully!'})
    return jsonify('success')

@app.route('/places', methods=['GET'])
def submit_form():
    # data = request.json
    # destination = data.get('destination')
    # category = data.get('category')
    # limit=data.get('limit')

    # api_place_url="https://api.geoapify.com/v1/geocode/search?text="

    # place_params = {
    #     'text': destination,
    #     'apiKey': api_key
    # }

    # headers = CaseInsensitiveDict()
    # headers["Accept"] = "application/json"

    # place_resp = requests.get(api_place_url, params=place_params, headers=headers)
    # place_data = place_resp.json()
    # place_id = place_data['results'][0]['place_id']

    # # resp = requests.get(api_place_url+destination.replace(" ","%20")+api_key, headers=headers)
    

    # api_url = "https://api.geoapify.com/v2/places?categories="
    # types_params = {
    #     'categories' : category,
    #     'place' : place_id,
    #     'limit' : limit,
    #     'apiKey' : api_key
    # }

    # headers = CaseInsensitiveDict()
    # headers["Accept"] = "application/json"

    # types_resp = requests.get(api_url, params=types_params, headers=headers)
    # types_data = types_resp.json()
    # types_locations = types_data['features']

    # places = []
    # for location in types_locations:
    #      places.append({
    #         'name': location['properties']['name'],
    #         'address': location['properties']['formatted'],
    #     })
    
    # return jsonify({'places': places})
    return jsonify({
        'status': 'success',
        'places': places})


if __name__ == '__main__':
    app.run()