import pytest
from unittest.mock import MagicMock
from app.blueprints.users.user_service import UserService
from app.blueprints.users.user_model import UserModel
from bson import ObjectId

@pytest.fixture
def mock_collection():
    """Crea un mock para la colección de MongoDB."""
    return MagicMock()

@pytest.fixture
def user_service(mock_collection):
    """Crea una instancia de UserService con una colección mockeada."""
    return UserService(mock_collection)

def test_get_all_users(user_service, mock_collection):
    """Prueba obtener todos los usuarios."""
    mock_users = [
        {"_id": ObjectId(), "name": "Daniela", "last_name": "Mendoza", "email": "daniela@test.com", "password": "password123"},
        {"_id": ObjectId(), "name": "Carlos", "last_name": "Perez", "email": "carlos@test.com", "password": "password456"}
    ]
    mock_collection.find.return_value = mock_users

    users = user_service.get_all_users()
    assert len(users) == 2
    assert users[0].name == "Daniela"
    assert users[1].email == "carlos@test.com"

def test_get_user_by_email_found(user_service, mock_collection):
    """Prueba obtener un usuario por email (usuario encontrado)."""
    mock_user = {"_id": ObjectId(), "name": "Daniela", "last_name": "Mendoza", "email": "daniela@test.com", "password": "password123"}
    mock_collection.find_one.return_value = mock_user

    user = user_service.get_user_by_email("daniela@test.com")
    assert user.name == "Daniela"
    assert user.email == "daniela@test.com"

def test_get_user_by_email_not_found(user_service, mock_collection):
    """Prueba obtener un usuario por email (usuario no encontrado)."""
    mock_collection.find_one.return_value = None

    with pytest.raises(Exception) as e:
        user_service.get_user_by_email("nonexistent@test.com")
    assert e.value.code == 404
    assert "user not found" in e.value.description

def test_create_user(user_service, mock_collection):
    """Prueba la creación de un usuario."""
    mock_collection.insert_one.return_value.inserted_id = ObjectId()
    user_data = {"name": "Daniela", "last_name": "Mendoza", "email": "daniela@test.com", "password": "password123"}

    user = user_service.create_user(user_data)
    assert user.name == "Daniela"
    assert user.email == "daniela@test.com"
    assert user.id is not None

def test_update_user_found(user_service, mock_collection):
    """Prueba actualizar un usuario existente."""
    mock_id = ObjectId()
    mock_user = {"_id": mock_id, "name": "Daniela", "last_name": "Mendoza", "email": "daniela@test.com", "password": "password123"}
    mock_collection.find_one.return_value = mock_user
    updated_data = {"name": "Daniela Updated", "last_name": "Mendoza"}

    user_service.update_user(str(mock_id), updated_data)
    mock_collection.update_one.assert_called_once_with(
        {"_id": mock_id}, {"$set": updated_data}
    )

def test_update_user_not_found(user_service, mock_collection):
    """Prueba actualizar un usuario que no existe."""
    mock_collection.find_one.return_value = None

    with pytest.raises(Exception) as e:
        user_service.update_user(str(ObjectId()), {"name": "No existe"})
    assert e.value.code == 404
    assert "user with id" in e.value.description

def test_delete_user_found(user_service, mock_collection):
    """Prueba eliminar un usuario existente."""
    mock_id = ObjectId()
    mock_user = {"_id": mock_id, "name": "Daniela"}
    mock_collection.find_one.return_value = mock_user

    user_service.delete_user(str(mock_id))
    mock_collection.delete_one.assert_called_once_with({"_id": mock_id})

def test_delete_user_not_found(user_service, mock_collection):
    """Prueba eliminar un usuario que no existe."""
    mock_collection.find_one.return_value = None

    with pytest.raises(Exception) as e:
        user_service.delete_user(str(ObjectId()))
    assert e.value.code == 404
    assert "user with id" in e.value.description
