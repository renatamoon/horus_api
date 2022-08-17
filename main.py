# STANDARD IMPORTS
from flask import Flask, request, Response, Request
from http import HTTPStatus


app = Flask(__name__)


@app.route('/get_data_from_lenovo_website', methods=["GET"])
def xxx():
    pass


if __name__ == '__main__':
    app.run(debug=True)