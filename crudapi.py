from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from helper_functions import *
from models import *

db_user = 'root'
db_user_password='pass'
db_hostname='localhost'
schema = 'andrewg'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{db_user}:{db_user_password}@{db_hostname}/{schema}' #db connection string for MySql
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.app = app
db.init_app(app)
db.create_all()

#create audio file api
@app.route('/fileserver/create_file', methods=['POST'])
def create_file():
    data_ = {'audioFileType':request.json['audioFileType'], **request.json['audioFileMetadata']}
    if not check_file_type(data_['audioFileType']):
        return '', 400
    if eval(f'validate_{data_["audioFileType"].lower()}')(data_):
        return '', 400
    insert_file(data_['audioFileType'], request.json)
    return '', 200

#fetch audio file(s) api
@app.route('/fileserver/get_file/<audioFileType>', defaults={'audioFileID': None}, methods=['GET'])
@app.route('/fileserver/get_file/<audioFileType>/<audioFileID>', methods=['GET'])
def get_file(audioFileType, audioFileID):
    data = get_audiofile(audioFileType, audioFileID)
    if len(data[0:]) == 0:
        return '', 400
    if not data:
        return '', 400
    return '', 200

#update audio file api
@app.route('/fileserver/update_file/<audioFileType>/<audioFileID>', methods=['POST'])
def update_file(audioFileType, audioFileID):
    if len(get_audiofile(audioFileType, audioFileID)[0:]) < 1: #check if file with suc id exist
        return '', 400
    update_audiofile(audioFileType, audioFileID, request.json)
    return '', 200

#delete audio file api
@app.route('/fileserver/delete_file/<audioFileType>/<audioFileID>', methods=['POST'])
def delete_file(audioFileType, audioFileID):
    if len(get_audiofile(audioFileType, audioFileID)[0:]) < 1: #check if file with suc id exist
        return '', 400
    delete_audiofile(audioFileType, audioFileID)
    return '', 200

    
    
if __name__ == '__main__':
    app.run(debug=True)
