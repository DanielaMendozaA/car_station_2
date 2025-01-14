# app/__init__.py o main.py
from flask import Flask, jsonify
from flask_cors import CORS
from app.extensions import marshInstance
from app.config import Config
from app.db_init import mongo, initialize_db
from app.errors.error_handling import handle_generic_error, handle_not_found_error, handle_unauthorized_error
from app.errors.database_errors import handle_database_errors, PyMongoError 


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Inicializa extensiones
    marshInstance.init_app(app)
    CORS(app)
    initialize_db(app)
    
    # Registrar blueprints
    from app.blueprints.users.user_route import user_bp
    app.register_blueprint(user_bp, url_prefix='/api/users')
    
    # Registro de manejadores de errores globales
    app.register_error_handler(Exception, handle_generic_error)
    app.register_error_handler(404, handle_not_found_error) 
    app.register_error_handler(401, handle_unauthorized_error) 
    app.register_error_handler(PyMongoError, handle_database_errors) 
    
    return app

    