import json

from flask import Flask, jsonify, request
from flask_cors import CORS
from loger import Logger
from sql_logik import get_ids_from_database_by_let, get_all_by_id, get_name_by_id

port = 1234
host = "0.0.0.0"
name = __name__

app = Flask(name)
CORS(app)
loge = Logger("web.log")

@app.route("/search", methods=['get'])
def serch():
    ser = request.args.get('name')
    if ser != None:
        ids = get_ids_from_database_by_let(ser)
        print(ids)
        dt = []
        for i in ids:
            #bobik = {"name": get_name_by_id(i), "id": i}
            dt.append(get_name_by_id(i))

        print(json.dumps(dt, ensure_ascii=False))
        return jsonify(dt)
    else:
        return 'None'

@app.route("/medicine/<id>/id", methods=['get'])
def get_data(id):
    try:
        ser = int(id)
    except:
        return "ERROR"
    dt = get_all_by_id(ser)
    print(json.dumps(dt, ensure_ascii=False))
    return jsonify(dt)

@app.route("/medicine/<name>/name", methods=['get'])
def gete_data(name):
    ser = get_ids_from_database_by_let(name)[0]
    dt = get_all_by_id(ser)
    dt["href"] = "https://www.vidal.ru" + dt["href"]
    print(json.dumps(dt, ensure_ascii=False))
    return jsonify(dt)

app.run(port=port, host=host, debug=True)

# /search?name=sdfsdfsdf
# /medicine/ID/report