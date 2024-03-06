from flask import Flask, make_response, jsonify
from db import connection

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users():
    if connection:
        return make_response(
            jsonify("entrou com sucesso")
        )
    else:
        return make_response(
            jsonify("nao funciona")
        )

app.run()