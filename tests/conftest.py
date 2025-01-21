import pytest
from app import create_app

@pytest.fixture
def app():
    """Crea una instancia de la aplicación Flask para pruebas."""
    app = create_app()
    app.config.update({
        "TESTING": True,  # Habilita el modo de testing
        "MONGO_URI": "mongodb://localhost:27017/test_db",  # Usar una DB separada para pruebas
    })
    yield app

@pytest.fixture
def client(app):
    """Proporciona un cliente de pruebas para la aplicación."""
    return app.test_client()
