from flask import Flask, request
import json
from flask_cors import CORS
from MongoAccess import Database
from AES_Encrypt_Decrypt import DataProtection


app = Flask(__name__)
CORS(app)
MongoClass = Database()
AESClass = DataProtection()


@app.route('/add-note', methods=['POST'])
def add_note():

    if MongoClass.user_input(AESClass.aes_encryption(request.get_json()['content'].encode())):
        return {'status': 'ok', 'message': 'Your note has been added!'}
    else:
        return {'status': 'error', 'message': 'Oops, something went wrong!'}


@app.route('/get-notes', methods=['GET'])
def get_notes():
    return json.dumps(MongoClass.give_me_my_notes())


@app.route('/clear-all', methods=['DELETE'])
def clear_all():
    if MongoClass.clean_this_mess_up():
        return {'status': 'Ok', 'message': 'Your notes have been cleared!'}
    else:
        return {'status': 'error', 'message': 'Oops, something went wrong!'}


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8084)
