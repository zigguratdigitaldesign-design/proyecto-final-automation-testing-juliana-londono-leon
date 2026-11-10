import pytest
import json
import os
from pages.login_page import LoginPage
from utils.logger import setup_logger

logger = setup_logger()

def load_test_data():
    """Carga los datos de prueba desde el archivo JSON."""
    data_path = os.path.join(os.path.dirname(__file__), '../../data/users_data.json')
    with open(data_path, 'r', encoding='utf-8') as f:
        return json.load(f)

@pytest.mark.ui
class TestLogin:
    """Tests de login parametrizados con datos externos."""
    
    @pytest.mark.parametrize("test_data", load_test_data())
    def test_login_flows(self, setup_ui, test_data):
        """
        Test parametrizado que cubre:
        - Login exitoso
        - Login con password incorrecto
        - Login con email inválido
        """
        logger.info(f"=== Ejecutando: {test_data['test_name']} ===")
        
        # Arrange
        login_page = LoginPage(setup_ui)
        login_page.navigate()
        
        # Act
        login_page.login(test_data['email'], test_data['password'])
        
        # Assert
        if test_data['expected_result'] == 'success':
            assert login_page.is_login_successful(), "El login debería ser exitoso"
            logger.info("✓ Login exitoso verificado")
        else:
            error_msg = login_page.get_error_message()
            assert error_msg == test_data['expected_message'], \
                f"Mensaje de error incorrecto. Esperado: {test_data['expected_message']}, Obtenido: {error_msg}"
            logger.info(f"✓ Error esperado verificado: {error_msg}")