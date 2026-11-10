import pytest
from utils.api_client import APIClient
from utils.logger import setup_logger

logger = setup_logger()

@pytest.mark.api
class TestDeleteUsers:
    """Tests de API - Método DELETE para eliminar usuarios."""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Configura el cliente API antes de cada test."""
        self.client = APIClient()
    
    def test_delete_existing_user(self):
        """
        Caso de prueba API #3a: Eliminar usuario existente
        - Realizar DELETE a /api/users/{id}
        - Validar código de estado 204 (No Content)
        """
        logger.info("=== Eliminar usuario existente ===")
        
        # Act: Realizar la petición DELETE
        response = self.client.delete("/api/users/2")
        
        # Assert: Validar código de estado
        assert response.status_code == 204, \
            f"Se esperaba status 204, se obtuvo {response.status_code}"
        
        # Assert: Validar que no hay contenido en la respuesta
        assert response.text == "", "La respuesta debe estar vacía (204 No Content)"
        
        logger.info("✓ Usuario eliminado exitosamente (204 No Content)")
    
    def test_delete_nonexistent_user(self):
        """
        Caso de prueba API #3b: Eliminar usuario inexistente
        - Realizar DELETE a /api/users/{id} con ID inexistente
        - Validar código de estado (ReqRes devuelve 204 incluso para IDs inexistentes)
        """
        logger.info("=== Eliminar usuario inexistente ===")
        
        # Act: Realizar la petición DELETE
        response = self.client.delete("/api/users/99999")
        
        # Assert: Validar código de estado
        # ReqRes devuelve 204 incluso para IDs inexistentes (comportamiento de la API)
        assert response.status_code == 204, \
            f"Se esperaba status 204, se obtuvo {response.status_code}"
        
        logger.info("✓ DELETE manejado correctamente (API devuelve 204 incluso para IDs inexistentes)")
    
    def test_create_and_delete_user(self):
        """
        Caso de prueba API #3c: Flujo completo - Crear y eliminar usuario
        - Crear un usuario con POST
        - Eliminar el usuario con DELETE
        - Validar ambos códigos de estado
        """
        logger.info("=== Flujo completo: Crear y eliminar usuario ===")
        
        # Arrange: Datos del nuevo usuario
        new_user_data = {
            "name": "User to Delete",
            "job": "Temporary Position"
        }
        
        # Act 1: Crear el usuario
        create_response = self.client.post("/api/users", data=new_user_data)
        assert create_response.status_code == 201, "La creación del usuario falló"
        
        created_user = create_response.json()
        user_id = created_user['id']
        logger.info(f"Usuario creado con ID: {user_id}")
        
        # Act 2: Eliminar el usuario
        delete_response = self.client.delete(f"/api/users/{user_id}")
        
        # Assert: Validar que la eliminación fue exitosa
        assert delete_response.status_code == 204, \
            f"Se esperaba status 204, se obtuvo {delete_response.status_code}"
        
        logger.info(f"✓ Usuario {user_id} eliminado exitosamente")