from flask import abort
from app.blueprints.users.user_model import UserModel
from pymongo.collection import Collection
from bson import ObjectId  

class UserService:
    def __init__(self, collection: Collection):
        self.collection = collection
    
    def get_all_users(self):
        users = self.collection.find()
        return[UserModel.from_dict(user) for user in users]
    
    def get_user_by_email(self, email):
        user = self.collection.find_one({
            "email": email
        })
        print("user db",user)
        if user is None:
            abort(404, description="user not found")
        return UserModel.from_dict(user)
    
    
    def create_user(self, user):
        result  = self.collection.insert_one(user)
        return UserModel.from_dict({
                 "_id": result.inserted_id,
                "name": user["name"],
                "last_name": user["last_name"], 
                "email": user["email"], 
                "password": user["password"]
            })
    
    def update_user(self, id: str, user_data):
        user = self.collection.find_one({
            "_id": ObjectId(id)
        })
        if user is None:
            abort(404, description=f"user with id: {id} not found")
            
        result = self.collection.update_one(
            {"_id": ObjectId(id)},  # Filtro para encontrar el documento
            {"$set": user_data}          # Actualiza solo los campos incluidos en `user`
        )
        
        print("este es el result de update", result)
        
        user_updated = self.collection.find_one({
            "_id": ObjectId(id)
        })
        return UserModel.from_dict(user_updated)
    
    def delete_user(self, id: str):
        user = self.collection.find_one({
            "_id": ObjectId(id)
        })
        if user is None:
            abort(404, description=f"user with id: {id} not found")
        
        result = self.collection.delete_one({
            "_id": ObjectId(id)
        })
        return result
        
        
        
        
    
          
        
