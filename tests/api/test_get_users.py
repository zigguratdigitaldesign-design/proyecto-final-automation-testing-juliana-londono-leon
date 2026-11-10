import pytest
import json
import os
from utils.api_client import APIClient
from utils.logger import setup_logger

logger = setup_logger()

def load_api_data():
    """Carga los datos de prueba desde el archivo JSON."""
    data_path = os.path.join(os.path.dirname(__file__), '../../data/api_data.json')
    with open(data_path, 'r', encoding='utf-8') as f:
        return json.load(f)

@pytest.mark.api
class TestGetUsers:
    """Tests de API - Método GET para obtener usuarios."""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Configura el cliente API antes de cada test."""
        self.client = APIClient()
    
    @pytest.mark.parametrize("user_data", load_api_data()['valid_users'])
    def test_get_existing_user(self, user_data):
        """
        Caso de prueba API #1a: Obtener usuario existente
        - Realizar GET a /api/users/{id}
        - Validar código de estado 200
        - Validar estructura JSON
        - Validar contenido específico
        """
        logger.info(f"=== {user_data['test_name']} ===")
        
        # Act: Realizar la petición GET
        response = self.client.get(f"/api/users/{user_data['user_id']}")
        
        # Assert: Validar código de estado
        assert response.status_code == user_data['expected_status'], \
            f"Se esperaba status {user_data['expected_status']}, se obtuvo {response.status_code}"
        
        # Assert: Validar estructura JSON
        response_json = response.json()
        assert 'data' in response_json, "La respuesta debe contener la clave 'data'"
        assert 'id' in response_json['data'], "El objeto data debe contener 'id'"
        assert 'email' in response_json['data'], "El objeto data debe contener 'email'"
        assert 'first_name' in response_json['data'], "El objeto data debe contener 'first_name'"
        assert 'last_name' in response_json['data'], "El objeto data debe contener 'last_name'"
        
        # Assert: Validar contenido específico
        assert response_json['data']['email'] == user_data['expected_name'], \
            f"Email incorrecto. Esperado: {user_data['expected_name']}"
        
        logger.info(f"✓ Usuario {user_data['user_id']} obtenido correctamente")
    
    @pytest.mark.parametrize("user_data", load_api_data()['invalid_users'])
    def test_get_nonexistent_user(self, user_data):
        """
        Caso de prueba API #1b: Obtener usuario inexistente
        - Realizar GET a /api/users/{id} con ID inexistente
        - Validar código de estado 404
        """
        logger.info(f"=== {user_data['test_name']} ===")
        
        # Act: Realizar la petición GET
        response = self.client.get(f"/api/users/{user_data['user_id']}")
        
        # Assert: Validar código de estado
        assert response.status_code == user_data['expected_status'], \
            f"Se esperaba status {user_data['expected_status']}, se obtuvo {response.status_code}"
        
        logger.info(f"✓ Usuario inexistente manejado correctamente (404)")
    
    def test_get_list_of_users(self):
        """
        Caso de prueba API #1c: Obtener lista de usuarios
        - Realizar GET a /api/users?page=1
        - Validar código de estado 200
        - Validar que la lista contiene usuarios
        - Validar estructura de paginación
        """
        logger.info("=== Obtener lista de usuarios ===")
        
        # Act: Realizar la petición GET
        response = self.client.get("/api/users", params={"page": 1})
        
        # Assert: Validar código de estado
        assert response.status_code == 200, \
            f"Se esperaba status 200, se obtuvo {response.status_code}"
        
        # Assert: Validar estructura JSON
        response_json = response.json()
        assert 'data' in response_json, "La respuesta debe contener la clave 'data'"
        assert 'page' in response_json, "La respuesta debe contener la clave 'page'"
        assert 'per_page' in response_json, "La respuesta debe contener la clave 'per_page'"
        assert 'total' in response_json, "La respuesta debe contener la clave 'total'"
        assert 'total_pages' in response_json, "La respuesta debe contener la clave 'total_pages'"
        
        # Assert: Validar que hay usuarios en la lista
        assert len(response_json['data']) > 0, "La lista de usuarios no debe estar vacía"
        assert response_json['page'] == 1, "La página debe ser 1"
        
        logger.info(f"✓ Lista de usuarios obtenida: {len(response_json['data'])} usuarios")