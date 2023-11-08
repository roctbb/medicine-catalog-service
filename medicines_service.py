from flask import jsonify, request
from manage import *
from methods import *


@app.route("/search", methods=['get'])
def search():
    query = request.args.get('title')

    if query and len(query) >= 2:
        results = find_by_name(query)
        return jsonify([{
            "id": result.id,
            "title": result.title,
        } for result in results])
    else:
        return jsonify([])


@app.route("/medicine/<id>", methods=['get'])
def get_data(id):
    try:
        ser = int(id)
    except:
        return "ERROR"
    dt = get_by_id(ser)
    dt["href"] = "https://www.vidal.ru" + dt["href"]

    return jsonify(dt)


if __name__ == "__main__":
    app.run(port=PORT, host=HOST, debug=True)
