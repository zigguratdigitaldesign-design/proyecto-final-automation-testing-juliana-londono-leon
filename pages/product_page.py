from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import setup_logger

logger = setup_logger()

class ProductPage(BasePage):
    """Page Object para la página de detalle de producto."""
    
    # Locators
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product-information h2")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product-information span span")
    PRODUCT_CATEGORY = (By.CSS_SELECTOR, ".product-information p:nth-child(3)")
    QUANTITY_INPUT = (By.CSS_SELECTOR, "#quantity")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.cart")
    SUCCESS_MODAL = (By.CSS_SELECTOR, ".modal-content")
    VIEW_CART_LINK = (By.CSS_SELECTOR, ".modal-content u")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def get_product_name(self):
        """Obtiene el nombre del producto."""
        return self.get_text(*self.PRODUCT_NAME)
    
    def get_product_price(self):
        """Obtiene el precio del producto."""
        return self.get_text(*self.PRODUCT_PRICE)
    
    def set_quantity(self, quantity):
        """Establece la cantidad del producto."""
        logger.info(f"Estableciendo cantidad: {quantity}")
        self.send_keys(*self.QUANTITY_INPUT, str(quantity))
    
    def add_to_cart(self):
        """Agrega el producto al carrito."""
        logger.info("Agregando producto al carrito")
        self.click(*self.ADD_TO_CART_BUTTON)
    
    def is_success_modal_displayed(self):
        """Verifica si aparece el modal de éxito."""
        return self.is_element_present(*self.SUCCESS_MODAL)
    
    def go_to_cart_from_modal(self):
        """Navega al carrito desde el modal."""
        logger.info("Navegando al carrito desde el modal")
        self.click(*self.VIEW_CART_LINK)