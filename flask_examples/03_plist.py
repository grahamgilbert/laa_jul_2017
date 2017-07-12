from flask import Flask
from plistlib import writePlistToString
app = Flask(__name__)

@app.route('/plist')
def gimmie_json():
    output = {
        'Name': 'Cannonball',
        'Brewery': 'Magic Rock',
        'Style': 'American IPA'
    }
    return writePlistToString(output)
