import pytest
import json
import os
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.search_page import SearchPage
from utils.logger import setup_logger

logger = setup_logger()

def load_search_data():
    """Carga los datos de búsqueda desde el archivo JSON."""
    data_path = os.path.join(os.path.dirname(__file__), '../../data/search_data.json')
    with open(data_path, 'r', encoding='utf-8') as f:
        return json.load(f)

@pytest.mark.ui
class TestSearch:
    """Tests de búsqueda de productos."""
    
    @pytest.mark.parametrize("search_data", load_search_data())
    def test_search_product(self, setup_ui, search_data):
        """
        Caso de prueba #2: Búsqueda de productos
        - Login exitoso
        - Búsqueda de producto
        - Verificación de resultados
        """
        logger.info(f"=== Test de búsqueda: {search_data['test_name']} ===")
        
        # Arrange: Login primero
        login_page = LoginPage(setup_ui)
        login_page.navigate()
        login_page.login("test_user@example.com", "Test123!")
        
        home_page = HomePage(setup_ui)
        assert home_page.is_user_logged_in(), "El usuario debería estar logueado"
        
        # Act: Buscar producto
        home_page.search_product(search_data['search_term'])
        search_page = SearchPage(setup_ui)
        
        # Assert: Verificar resultados
        if search_data['expected_results'] > 0:
            assert search_page.are_results_displayed(), "Deberían mostrarse resultados"
            results_count = search_page.get_search_results_count()
            assert results_count > 0, f"Se esperaban resultados para '{search_data['search_term']}'"
            logger.info(f"✓ Búsqueda exitosa: {results_count} productos encontrados")
        else:
            assert search_page.is_no_results_message_displayed() or not search_page.are_results_displayed(), \
                "No deberían mostrarse resultados"
            logger.info(f"✓ Búsqueda sin resultados como se esperaba")