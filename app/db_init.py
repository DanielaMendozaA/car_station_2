from flask_pymongo import PyMongo

mongo = PyMongo()

def initialize_db(app):
    mongo.init_app(app)
    with app.app_context():
        mongo.db.users.create_index("email", unique=True)
