from flask import Blueprint, request, jsonify
from app.blueprints.users.user_dto import user_dto, update_user_dto
from app.blueprints.users.user_service import UserService
from app import mongo
from app.utils.successful_response import success_response
from marshmallow import ValidationError


user_bp = Blueprint('user', __name__)

@user_bp.route('/', methods=['GET'])
def get_all_users():
    user_service = UserService(mongo.db.users)
    users = user_service.get_all_users()
    return jsonify([user.to_dict() for user in users])

@user_bp.route('/<email>', methods=['GET'])
def get_user(email):
    user_service = UserService(mongo.db.users)
    user = user_service.get_user_by_email(email)
    print("user in route", user)
    return jsonify(user.to_dict())

@user_bp.route('/', methods=['POST'])
def create_user():
    try:
        user_service = UserService(mongo.db.users)
        data = user_dto.load(request.json)
        user = user_service.create_user(data)
        print("esta es el user despues de service", user, type(user))

        return success_response(
            {
                "id": str(user.id),
                "name": user.name,
                "last_name": user.last_name,
                "email": user.email
            },
            message="User created successfully",
            status_code=201
        )

    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

@user_bp.route('/<id>', methods=['PUT'])
def update_user(id):
    try:
        user_service = UserService(mongo.db.users)
        data = update_user_dto.load(request.json)
        user_updated = user_service.update_user(id, data)
        return success_response(
            user_updated.to_dict(),  # Convierte el objeto en un diccionario
            message="User updated successfully", 
            status_code=200
        )
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    
@user_bp.route('/<id>', methods=['DELETE'])
def delete_user(id):
    user_service = UserService(mongo.db.users)
    result = user_service.delete_user(id)
    return success_response({}, message="user deleted successfully", status_code=200)









