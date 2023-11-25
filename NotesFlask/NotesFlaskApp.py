from flask import Flask, request
import json
import MongoAccess as monots

app = Flask(__name__)


@app.route('/get-notes', methods=['GET'])
def get_notes():
    return json.dumps(monots.give_me_my_notes())


@app.route('/add-note', methods=['POST'])
def add_note():
    if monots.user_input(request.get_json()['content']):
        return {'status': 'Ok'}
    else:
        return {'status': 'error', 'message': 'Oops, something went wrong!'}


@app.route('/clear-all', methods=['DELETE'])
def clear_all():
    return monots.clean_this_mess_up()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8084)
