from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def NoteApp():
    pass


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8084)
