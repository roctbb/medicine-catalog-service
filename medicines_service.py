import json

from flask import Flask, jsonify, request
from flask_cors import CORS
from logger import Logger
from sql_logik import *

port = 5574
host = "0.0.0.0"
name = __name__

app = Flask(name)
CORS(app)
loge = Logger("web.log")


@app.route("/search", methods=['get'])
def search():
    query = request.args.get('name')

    if query and len(query) >= 3:
        results = get_by_query(query)

        return jsonify([{
            "id": result[0],
            "title": result[5],
        } for result in results])
    else:
        return jsonify([])


@app.route("/medicine/<id>", methods=['get'])
def get_data(id):
    try:
        ser = int(id)
    except:
        return "ERROR"
    dt = get_all_by_id(ser)
    dt["href"] = "https://www.vidal.ru" + dt["href"]

    return jsonify(dt)


if __name__ == "__main__":
    app.run(port=port, host=host, debug=True)
