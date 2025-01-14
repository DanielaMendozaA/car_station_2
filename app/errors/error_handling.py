from flask import jsonify
from werkzeug.exceptions import HTTPException

def handle_generic_error(error):
    response = {
        "status": "error",
        "message": str(error),
    }
    return jsonify(response), 500

def handle_not_found_error(error):
    response = {
        "status": "error",
        "message": f"Resource not found: {str(error)}",
    }
    return jsonify(response), 404

def handle_unauthorized_error(error):
    response = {
        "status": "error",
        "message": f"Unauthorized access: {str(error)}",
    }
    return jsonify(response), 401

def handle_badrequest_error(error):
    response = {
        "status": "error",
        "message": f"Bad Request: {str(error)}",
    }
    return jsonify(response), 400
