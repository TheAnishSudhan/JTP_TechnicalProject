from flask import Flask, jsonify, request, render_template, abort
from flask_cors import CORS, cross_origin 
from ner import recommend_place
app = Flask(__name__)
app.config.from_object(__name__)

CORS(app)


import requests
from requests.structures import CaseInsensitiveDict

cumulative_recommendations = ['x']

@app.route('/places', methods=['GET'])
def submit_form():
    recommendations = recommend_place(cumulative_recommendations[0])

    # For testing purposes
    # recommendations = [{'Place': 'Hathee Singh Jain Temple', 'City': 'Ahmedabad', 'Raw_Review': 'Very old and known Temple.visited here many time with my colleagues Friends.Really wonderful temple, i want to again and again visit to here'}, {'Place': 'ISKCON Temple', 'City': 'Ahmedabad', 'Raw_Review': 'This temple is very beautiful temple. The temple is situated on SG highway road. I love this place. If you want peace of mind and soul.... you should definitely visit this temple.'}, {'Place': 'Ambalapuzha Sree Krishna Temple', 'City': 'Alappuzha', 'Raw_Review': 'Done miss it. It is a very nice place to visit. The deity is amazingly beautiful. And gives u the good old temple feel - typical south Indian old temple.'}, {'Place': 'Kankaria Lake', 'City': 'Ahmedabad', 'Raw_Review': "Don't miss to visit. Don't miss the baloon ride and the train ride. Clean. Perfect. Neat. Green. Value for money.whatever u want. U want to eat. Its here. U want to enjoy. Its here. U want thrill. Its here."}, {'Place': 'Agonda Beach', 'City': 'Agonda', 'Raw_Review': 'Agonda was fabulous.  If you want to party don’t go here but if you want to relax this is the place for you.'}, {'Place': 'Chand Baori (Step well)', 'City': 'Abhaneri', 'Raw_Review': 'If you are out to explore Rajasthan or visiting Jaipur…….. If you are fascinated towards old buildings, great architecture, want to click good pictures…or just want to go back in time ….then Abhaneri is the place to visit.\nIt was a Saturday, 10 in the...'}, {'Place': 'Luni River', 'City': 'Ajmer', 'Raw_Review': 'If you want to see high flow of water and want to take bath then go to this place and enjoy the beauty.'}, {'Place': 'Agra Fort', 'City': 'Agra', 'Raw_Review': "Cool, old historical site that we visited along with Taj Mahal in a day trip from Delhi. Magnificent old fort with fascinating history, if you like old historical sites it's a must-see."}, {'Place': 'Akshardham Temple', 'City': 'Ahmedabad', 'Raw_Review': 'It is ok. It is different temple. It is more show than a temple. One can not find internal peace there. One can not say it is a temple. If you want to visit for darshanam of God, it is not proper place. People like...'}, {'Place': 'Nanda Devi Temple', 'City': 'Almora', 'Raw_Review': 'This is an old temple which is very nice & clean and also very well maintained. If you can go there at evening time you can see the "Arati" which is great.Also, there is enough place inside the temple where you can sit and spend...'}]
  
    return jsonify({
            'status': 'success',
            'recommendations': recommendations})


@app.route('/nlp', methods=['POST', 'GET'])
def recommend():
    data = request.get_json()
    user_input=data.get('user_input')
    cumulative_recommendations[0] = user_input

    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(port=5001)