from flask import jsonify
from pymongo.errors import DuplicateKeyError, OperationFailure, PyMongoError

def handle_database_errors(error):
    
    if isinstance(error, DuplicateKeyError):
        response = {
            "status": "error",
            "message": f"Duplicate key error: {str(error)}"
        }
        return jsonify(response), 409  # Conflict
    
    elif isinstance(error, OperationFailure):  # General MongoDB operation failure (Cualquier otro error de operación)
        response = {
            "status": "error",
            "message": f"MongoDB operation failed: {str(error)}"
        }
        return jsonify(response), 500  # Internal Server Error
    
    elif isinstance(error, PyMongoError):  # Error genérico de PyMongo
        response = {
            "status": "error",
            "message": f"MongoDB error: {str(error)}"
        }
        return jsonify(response), 500  # Internal Server Error
    
    elif hasattr(error, 'code'):
        if error.code == 11000:  # MongoDB Duplicate Key Error
            response = {
                "status": "error",
                "message": f"Duplicate Key Error: {str(error)}"
            }
            return jsonify(response), 409  # 409 Conflict
        elif error.code == 121:  # MongoDB Document Validation Failure
            response = {
                "status": "error",
                "message": f"Document validation failure: {str(error)}"
            }
            return jsonify(response), 400  # Bad Request
        elif error.code == 43:  # CursorNotFound
            response = {
                "status": "error",
                "message": f"Cursor not found: {str(error)}"
            }
            return jsonify(response), 404  # Not Found

    # Si el error no coincide con los casos anteriores, se maneja como un error general de MongoDB
    response = {
        "status": "error",
        "message": f"MongoDB error: {str(error)}"
    }
    return jsonify(response), 500  # Internal Server Error
