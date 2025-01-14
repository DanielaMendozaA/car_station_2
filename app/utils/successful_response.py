from flask import jsonify


def success_response(data, message, status_code=200):
    response = { 
            "message": message, 
            "status": "success",
            "data": data }
    return jsonify(response), status_code