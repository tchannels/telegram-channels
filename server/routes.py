from flask import json, jsonify, request

from main import app
from Models import db
# TODO: try to make "from Models import Channels" as valid import
from Models.channels import Channels

@app.route('/')
def index():
    return jsonify({'result': 'Why are you here?'})

@app.route('/channels')
def get_channels():
    # TODO: navigation by cursor
    limit = request.json.get('limit') or 50
    offset = request.json.get('offset') or 0
    result = db.session.execute('''
        SELECT
            "id", "channel_id", "title", "image_link", "description"
        FROM "channels" 
        LIMIT :limit OFFSET :offset
    ''', {'limit': limit, 'offset': offset})
    
    channels = [dict(x) for x in result]
    return jsonify(channels)
