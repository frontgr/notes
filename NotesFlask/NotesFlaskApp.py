from flask import Flask, request
import json
from flask_cors import CORS
import MongoAccess as monots


app = Flask(__name__)
CORS(app)


@app.route('/add-note', methods=['POST'])
def add_note():
    from AES_Encrypt_Decrypt import aes_encryption

    if monots.user_input(aes_encryption(request.get_json()['content'].encode())):
        return {'status': 'Your note has been added!'}
    else:
        return {'status': 'error', 'message': 'Oops, something went wrong!'}


@app.route('/get-notes', methods=['GET'])
def get_notes():
    return json.dumps(monots.give_me_my_notes())


@app.route('/clear-all', methods=['DELETE'])
def clear_all():
    return monots.clean_this_mess_up()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8084)
