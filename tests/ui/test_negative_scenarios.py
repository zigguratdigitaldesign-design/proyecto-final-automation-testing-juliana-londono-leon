import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage
from utils.logger import setup_logger

logger = setup_logger()

@pytest.mark.ui
class TestNegativeScenarios:
    """Tests de escenarios negativos."""
    
    def test_login_with_empty_credentials(self, setup_ui):
        """
        Caso de prueba #5a: Login con credenciales vacías
        - Intentar login sin email ni password
        - Verificar que no se permite el login
        """
        logger.info("=== Test: Login con credenciales vacías ===")
        
        # Arrange
        login_page = LoginPage(setup_ui)
        login_page.navigate()
        
        # Act: Intentar login sin credenciales
        login_page.login("", "")
        
        # Assert: Debería permanecer en la página de login
        assert "/login" in setup_ui.current_url, "Debería permanecer en la página de login"
        logger.info("✓ Login con credenciales vacías bloqueado correctamente")
    
    def test_access_cart_without_login(self, setup_ui):
        """
        Caso de prueba #5b: Intentar acceder al carrito sin login
        - Navegar directamente al carrito sin estar logueado
        - Verificar comportamiento (debería mostrar carrito vacío o redirigir)
        """
        logger.info("=== Test: Acceder al carrito sin login ===")
        
        # Arrange: No hacer login, ir directamente al carrito
        cart_page = CartPage(setup_ui)
        cart_page.navigate()
        
        # Assert: El carrito debería estar vacío o mostrar mensaje apropiado
        # Automation Exercise permite ver el carrito sin login, pero estará vacío
        is_empty = cart_page.is_cart_empty() or cart_page.get_items_count() == 0
        assert is_empty, "El carrito debería estar vacío sin login"
        logger.info("✓ Carrito vacío verificado sin login")
    
    def test_search_nonexistent_product(self, setup_ui):
        """
        Caso de prueba #5c: Buscar producto inexistente
        - Login exitoso
        - Buscar producto que no existe
        - Verificar mensaje apropiado o ausencia de resultados
        """
        logger.info("=== Test: Buscar producto inexistente ===")
        
        # Arrange: Login
        login_page = LoginPage(setup_ui)
        login_page.navigate()
        login_page.login("test_user@example.com", "Test123!")
        
        home_page = HomePage(setup_ui)
        assert home_page.is_user_logged_in(), "El usuario debería estar logueado"
        
        # Act: Buscar producto inexistente
        home_page.search_product("xyznonexistentproduct12345")
        
        # Assert: No deberían mostrarse resultados o aparecer mensaje
        from pages.search_page import SearchPage
        search_page = SearchPage(setup_ui)
        
        # Verificar que no hay resultados o hay mensaje de "no encontrado"
        no_results = search_page.is_no_results_message_displayed() or search_page.get_search_results_count() == 0
        assert no_results, "No deberían mostrarse resultados para producto inexistente"
        logger.info("✓ Búsqueda de producto inexistente manejada correctamente")