import requests
from flask import Flask, request, render_template

app = Flask(__name__)

NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/find_doctor', methods=['POST'])
def find_doctor():
    latitude = request.form['latitude']
    longitude = request.form['longitude']
    symptom = request.form['symptom']
    
    # Call Nominatim API to find nearby hospitals
    params = {
        'q': 'hospital',
        'format': 'json',
        'limit': 10,
        'lat': latitude,
        'lon': longitude
    }
    
    try:
        response = requests.get(NOMINATIM_URL, params=params)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        data = []
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
        data = []
    except ValueError as json_err:
        print(f"JSON decode error occurred: {json_err}")
        print("Response text was:", response.text)
        data = []
    
    # Process the response to extract necessary information
    places = []
    for place in data:
        places.append({
            "name": place.get('display_name', 'Unknown'),
            "lat": place.get('lat'),
            "lng": place.get('lon')
        })
    
    return render_template('results.html', latitude=latitude, longitude=longitude, places=places)

if __name__ == '__main__':
    app.run(debug=True, port=5003)