class UserModel:
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
    
    @classmethod
    def from_dict(cls, data):
        return cls(id=str(data["_id"]), name=data["name"], email=data["email"], password=data["password"])

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email, "password": self.password}
