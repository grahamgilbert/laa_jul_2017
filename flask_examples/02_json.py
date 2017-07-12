from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route('/json')
def gimmie_json():
    output = {
        'Name': 'Black Betty',
        'Brewery': 'Beavertown',
        'Style': 'Black IPA'
    }
    return jsonify(output)
