import json
import requests
from flask import Flask, abort
app = Flask(__name__)

@app.route('/lost_stolen/<serial>')
def get_lost_stolen_status(serial):
    # This will query WHD shortly, but right now we just return a json dict
    device = query_inventory(serial)
    output = {}

    if device['status'] == 'Lost / Stolen':
        output['classes'] = ['macdestroyer']
    else:
        abort(404)
    return json.dumps(output)

@app.route('/encryption_required/<serial>')
def encryption_required(serial):
    # This will query WHD shortly, but right now we just return a json dict
    device = query_inventory(serial)
    output = {}

    if device['encryption_required'] == True:
        output['classes'] = ['crypt']
    else:
        abort(404)
    return json.dumps(output)

@app.route('/windows_vm/<serial>')
def get_windows_assignment(serial):
    device = query_inventory(serial)
    output = {}

    if device['windows_vm'] == True:
        output['munki::managed_installs'] = ['windows10_vm']
    else:
        abort(404)
    return json.dumps(output)

@app.route('/')
def hello_world():
    return 'Nothing to see here...'

def make_api_call(url, query_params={}):
    """
    Makes a call to basicinventory
    """
    # try:
    request = requests.get(url, params=query_params)
    returned_json = request.json()
    try:
        return returned_json
    except:
        return False

def query_inventory(serial):
    """
    Returns a dictionary of information about the device
    """
    ASSETS_URL = 'http://192.168.33.11/api/machines/{}/'.format(serial)
    output = {}
    asset_list = make_api_call(ASSETS_URL)
    if asset_list:
        return asset_list

    return output
