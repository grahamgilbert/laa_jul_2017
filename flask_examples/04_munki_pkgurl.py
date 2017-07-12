from flask import Flask
from flask import request
from flask import jsonify
app = Flask(__name__)

@app.route('/get_munki_pkgurl', methods=['GET'])
def get_munki_pkgurl():
    munki_pkg_urls = {
        '8.8.8.8': 'https://munki.company.com',
        '1.2.3.4': 'https://munki2.company.com',
        '127.0.0.1': 'http://localhost/munki_repo'
    }
    munki_server = munki_pkg_urls.get(
        request.remote_addr, 'https://munki.company.com')
    return jsonify({'munki_server': munki_server})
