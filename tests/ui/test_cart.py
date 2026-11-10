import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.product_page import ProductPage
from utils.logger import setup_logger

logger = setup_logger()

@pytest.mark.ui
class TestCart:
    """Tests del carrito de compras."""
    
    def test_add_product_to_cart(self, setup_ui):
        """
        Caso de prueba #3: Agregar producto al carrito
        - Login exitoso
        - Agregar primer producto al carrito
        - Verificar que el producto está en el carrito
        """
        logger.info("=== Test: Agregar producto al carrito ===")
        
        # Arrange: Login
        login_page = LoginPage(setup_ui)
        login_page.navigate()
        login_page.login("test_user@example.com", "Test123!")
        
        home_page = HomePage(setup_ui)
        assert home_page.is_user_logged_in(), "El usuario debería estar logueado"
        
        # Act: Agregar producto al carrito
        home_page.add_first_product_to_cart()
        
        # Assert: Verificar modal de éxito
        assert home_page.is_success_modal_displayed(), "Debería aparecer el modal de éxito"
        logger.info("✓ Producto agregado al carrito exitosamente")
        
        # Act: Ir al carrito
        home_page.go_to_cart_from_modal()
        cart_page = CartPage(setup_ui)
        
        # Assert: Verificar que hay al menos un producto en el carrito
        items_count = cart_page.get_items_count()
        assert items_count > 0, "El carrito debería tener al menos un producto"
        logger.info(f"✓ Carrito verificado: {items_count} producto(s)")
    
    def test_view_product_details_and_add_to_cart(self, setup_ui):
        """
        Caso de prueba #4: Ver detalle de producto y agregar al carrito
        - Login exitoso
        - Ver detalle del primer producto
        - Agregar al carrito con cantidad específica
        - Verificar en el carrito
        """
        logger.info("=== Test: Ver detalle y agregar al carrito ===")
        
        # Arrange: Login
        login_page = LoginPage(setup_ui)
        login_page.navigate()
        login_page.login("test_user@example.com", "Test123!")
        
        home_page = HomePage(setup_ui)
        assert home_page.is_user_logged_in(), "El usuario debería estar logueado"
        
        # Act: Ver detalle del producto
        home_page.view_first_product()
        product_page = ProductPage(setup_ui)
        
        # Obtener nombre del producto antes de agregarlo
        product_name = product_page.get_product_name()
        logger.info(f"Producto seleccionado: {product_name}")
        
        # Establecer cantidad y agregar al carrito
        product_page.set_quantity(2)
        product_page.add_to_cart()
        
        # Assert: Verificar modal de éxito
        assert product_page.is_success_modal_displayed(), "Debería aparecer el modal de éxito"
        logger.info("✓ Producto agregado al carrito desde detalle")
        
        # Act: Ir al carrito
        product_page.go_to_cart_from_modal()
        cart_page = CartPage(setup_ui)
        
        # Assert: Verificar que el producto está en el carrito
        assert cart_page.is_product_in_cart(product_name), \
            f"El producto '{product_name}' debería estar en el carrito"
        logger.info(f"✓ Producto '{product_name}' verificado en el carrito")