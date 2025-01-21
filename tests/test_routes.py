import pytest
from unittest.mock import MagicMock
from app.blueprints.users.user_service import UserService
from bson import ObjectId
from unittest.mock import MagicMock
from app.blueprints.users.user_model import UserModel


@pytest.fixture
def mock_user_service(mocker):
    """Mockea el servicio UserService."""
    mock_service = mocker.patch("app.blueprints.users.user_route.UserService")
    return mock_service.return_value


def test_get_all_users(client, mock_user_service):
    # mock_user_model = MagicMock()
    # mock_user_model.to_dict.side_effect = lambda: {
    #     "_id": "mock_id",
    #     "name": "Mock",
    #     "last_name": "User",
    #     "email": "mock@user.com"
    # }
    
    # mock_user_service.get_all_users.return_value = [mock_user_model]
    
    # Puede usarse la clase directamente ya que no tiene funciones muy complejas o que dependan de algo externo
    mock_users = [
        {"_id": ObjectId(), "name": "Daniela", "last_name": "Mendoza", "email": "daniela@test.com", "password": "password123"},
        {"_id": ObjectId(), "name": "Carlos", "last_name": "Perez", "email": "carlos@test.com", "password": "password456"},
    ]
    
    
    mock_user_service.get_all_users.return_value = [UserModel.from_dict(user) for user in mock_users]
    
    response = client.get("/api/users/")
    
    
    assert response.status_code == 200
    assert response.json[0]["name"] == "Daniela"


def test_get_user(client, mock_user_service):
    """Prueba la ruta GET /<email> (obtener usuario por email)."""   
    mock_user_model = MagicMock()
    mock_user_model.to_dict = lambda: {
        "_id": "mock_id",
        "name": "Daniela",
        "last_name": "Mendoza",
        "email": "daniela@test.com"
    }
    
    mock_user_service.get_user_by_email.return_value = mock_user_model
    
    
    

    response = client.get("/api/users/daniela@test.com")
    assert response.status_code == 200
    assert response.json["name"] == "Daniela"
    assert response.json["email"] == "daniela@test.com"


def test_create_user(client, mock_user_service):
    """Prueba la ruta POST / (crear usuario).""" 
    mock_user = {"_id": ObjectId(),
                 "name": "Daniela",
                 "last_name": "Mendoza",
                 "email": "daniela@test.com",
                 "password": "password123"}
    
    mock_user_service.create_user.return_value = UserModel.from_dict(mock_user)

    payload = {
        "name": "Daniela",
        "last_name": "Mendoza",
        "email": "daniela@test.com",
        "password": "password123"
    }
    response = client.post("/api/users/", json=payload)
    assert response.status_code == 201
    assert response.json["message"] == "User created successfully"
    assert response.json["status"] == "success"
    assert response.json["data"]["name"] == "Daniela"
    assert response.json["data"]["last_name"] == "Mendoza"
    assert response.json["data"]["email"] == "daniela@test.com"


def test_update_user(client, mock_user_service):
    """Prueba la ruta PUT /<id> (actualizar usuario)."""
    mock_user = {"_id": ObjectId(),
                 "name": "Daniela Updated", 
                 "last_name": "Mendoza",
                 "email": "daniela@test.com",
                 "password": "password123"}
    mock_user_service.update_user.return_value = UserModel.from_dict(mock_user)

    payload = {"name": "Daniela Updated", "last_name": "Mendoza"}
    response = client.put(f"/api/users/{mock_user['_id']}", json=payload)
    assert response.status_code == 200
    assert response.json["message"] == "User updated successfully"
    assert response.json["data"]["name"] == "Daniela Updated"


def test_delete_user(client, mock_user_service):
    """Prueba la ruta DELETE /<id> (eliminar usuario)."""
    mock_id = ObjectId()
    mock_user_service.delete_user.return_value = None

    response = client.delete(f"/api/users/{mock_id}")
    assert response.status_code == 200
    assert response.json["message"] == "user deleted successfully"
