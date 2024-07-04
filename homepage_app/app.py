from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load disease remedies from a JSON file
with open('disease_info.json', 'r') as f:
    disease_info = json.load(f)

@app.route('/', methods=['GET'])
def index():
    query = request.args.get('query')
    remedies = []
    image_url = None
    
    if query:
        query_lower = query.lower()
        disease_data = disease_info.get(query_lower, {})
        remedies = {
            'home_remedies': disease_data.get('home_remedies', []),
            'ayurvedic_remedies': disease_data.get('ayurvedic_remedies', [])
        }
        image_url = disease_data.get('image_url', None)
    
    return render_template('index.html', query=query, remedies=remedies, image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
