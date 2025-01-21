class UserModel:
    def __init__(self, id, name, last_name, email, password):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password
    
    @classmethod
    def from_dict(cls, data):
        return cls(id=str(data["_id"]),
                   name=data["name"],
                   last_name=data["last_name"],
                   email=data["email"],
                   password=data["password"])

    def to_dict(self):
        return {"id": self.id,
                "name": self.name,
                "last_name": self.last_name,
                "email": self.email,
                "password": self.password}
