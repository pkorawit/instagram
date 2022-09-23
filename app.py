from prediction import *
from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'title': 'Ads and Tourism filetering API',
                       'description': 'Ads and Tourism filetering API for Instagram data analytics'})

@app.route('/version')
def version():
    return jsonify({'version': '1.0',
                       'last-update': '23/09/2022 15:00:00'})


@app.route('/predict/<shortcode>')
def get_predict(shortcode):
    print(shortcode)
    result = predict(shortcode)
    print(result)
    return jsonify(result)

if __name__ == '__main__':
    # Only for debugging while developing
    server_port = os.environ.get('PORT', '5000')
    app.run(host='0.0.0.0', port=server_port)

