from app.blueprints.users.user_model import UserModel

def test_user_model_init():
    """Prueba la inicialización del modelo UserModel."""
    user = UserModel(
        id="123",
        name="Daniela",
        last_name="Mendoza",
        email="daniela@test.com",
        password="password123"
    )
    assert user.id == "123"
    assert user.name == "Daniela"
    assert user.last_name == "Mendoza"
    assert user.email == "daniela@test.com"
    assert user.password == "password123"

def test_user_model_from_dict():
    """Prueba el método from_dict del modelo UserModel."""
    data = {
        "_id": "123",
        "name": "Daniela",
        "last_name": "Mendoza",
        "email": "daniela@test.com",
        "password": "password123"
    }
    user = UserModel.from_dict(data)
    assert user.id == "123"
    assert user.name == "Daniela"
    assert user.last_name == "Mendoza"
    assert user.email == "daniela@test.com"
    assert user.password == "password123"

def test_user_model_to_dict():
    """Prueba el método to_dict del modelo UserModel."""
    user = UserModel(
        id="123",
        name="Daniela",
        last_name="Mendoza",
        email="daniela@test.com",
        password="password123"
    )
    user_dict = user.to_dict()
    assert user_dict == {
        "id": "123",
        "name": "Daniela",
        "last_name": "Mendoza",
        "email": "daniela@test.com",
        "password": "password123"
    }
