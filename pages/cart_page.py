from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import setup_logger

logger = setup_logger()

class CartPage(BasePage):
    """Page Object para la página del carrito de compras."""
    
    # Locators
    CART_ITEMS = (By.CSS_SELECTOR, "#cart_info_table tbody tr")
    PRODUCT_NAME = (By.CSS_SELECTOR, "td.cart_description h4 a")
    PRODUCT_QUANTITY = (By.CSS_SELECTOR, "td.cart_quantity button")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "td.cart_price p")
    PRODUCT_TOTAL = (By.CSS_SELECTOR, "td.cart_total p")
    PROCEED_TO_CHECKOUT_BUTTON = (By.CSS_SELECTOR, "a.btn-default.check_out")
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, "#empty_cart b")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://automationexercise.com/view_cart"
    
    def navigate(self):
        """Navega directamente a la página del carrito."""
        logger.info(f"Navegando a: {self.url}")
        self.driver.get(self.url)
    
    def get_items_count(self):
        """Obtiene la cantidad de productos en el carrito."""
        elements = self.driver.find_elements(*self.CART_ITEMS)
        count = len(elements)
        logger.info(f"Productos en el carrito: {count}")
        return count
    
    def get_first_product_name(self):
        """Obtiene el nombre del primer producto en el carrito."""
        return self.get_text(*self.PRODUCT_NAME)
    
    def get_first_product_price(self):
        """Obtiene el precio del primer producto."""
        return self.get_text(*self.PRODUCT_PRICE)
    
    def is_cart_empty(self):
        """Verifica si el carrito está vacío."""
        return self.is_element_present(*self.EMPTY_CART_MESSAGE)
    
    def proceed_to_checkout(self):
        """Hace clic en el botón de proceder al checkout."""
        logger.info("Procediendo al checkout")
        self.click(*self.PROCEED_TO_CHECKOUT_BUTTON)
    
    def is_product_in_cart(self, product_name):
        """Verifica si un producto específico está en el carrito."""
        items = self.driver.find_elements(*self.PRODUCT_NAME)
        for item in items:
            if product_name.lower() in item.text.lower():
                logger.info(f"Producto '{product_name}' encontrado en el carrito")
                return True
        logger.info(f"Producto '{product_name}' NO encontrado en el carrito")
        return False