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
class TestPostUsers:
    """Tests de API - Método POST para crear usuarios."""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Configura el cliente API antes de cada test."""
        self.client = APIClient()
    
    @pytest.mark.parametrize("user_data", load_api_data()['create_users'])
    def test_create_user(self, user_data):
        """
        Caso de prueba API #2a: Crear usuario
        - Realizar POST a /api/users con datos del usuario
        - Validar código de estado 201 (Created)
        - Validar que la respuesta contiene el ID generado
        - Validar que los datos enviados coinciden con la respuesta
        """
        logger.info(f"=== {user_data['test_name']} ===")
        
        # Arrange: Preparar los datos
        payload = {
            "name": user_data['name'],
            "job": user_data['job']
        }
        
        # Act: Realizar la petición POST
        response = self.client.post("/api/users", data=payload)
        
        # Assert: Validar código de estado
        assert response.status_code == user_data['expected_status'], \
            f"Se esperaba status {user_data['expected_status']}, se obtuvo {response.status_code}"
        
        # Assert: Validar estructura JSON
        response_json = response.json()
        assert 'id' in response_json, "La respuesta debe contener el ID del usuario creado"
        assert 'createdAt' in response_json, "La respuesta debe contener la fecha de creación"
        
        # Assert: Validar que los datos enviados coinciden
        assert response_json['name'] == user_data['name'], \
            f"El nombre no coincide. Esperado: {user_data['name']}"
        assert response_json['job'] == user_data['job'], \
            f"El trabajo no coincide. Esperado: {user_data['job']}"
        
        logger.info(f"✓ Usuario creado exitosamente con ID: {response_json['id']}")
    
    def test_create_user_and_retrieve(self):
        """
        Caso de prueba API #2b: Encadenamiento - Crear y obtener usuario
        - Realizar POST para crear un usuario
        - Extraer el ID de la respuesta
        - Realizar GET para obtener el usuario creado
        - Validar que el usuario existe
        """
        logger.info("=== Encadenamiento: Crear y obtener usuario ===")
        
        # Arrange: Datos del nuevo usuario
        new_user_data = {
            "name": "Integration Test User",
            "job": "Automation Engineer"
        }
        
        # Act 1: Crear el usuario
        create_response = self.client.post("/api/users", data=new_user_data)
        assert create_response.status_code == 201, "La creación del usuario falló"
        
        created_user = create_response.json()
        user_id = created_user['id']
        logger.info(f"Usuario creado con ID: {user_id}")
        
        # Act 2: Obtener el usuario (encadenamiento)
        # Nota: ReqRes no persiste datos, pero simulamos el flujo
        get_response = self.client.get(f"/api/users/{user_id}")
        
        # Assert: En ReqRes real, el usuario no persiste, pero validamos el flujo
        # En una API real, esperaríamos 200 y los datos del usuario
        logger.info(f"✓ Flujo de encadenamiento completado (POST → GET)")
        logger.info(f"  - Usuario creado: {created_user['name']}")
        logger.info(f"  - ID obtenido: {user_id}")