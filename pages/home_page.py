from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import setup_logger

logger = setup_logger()

class HomePage(BasePage):
    """Page Object para la página principal de Automation Exercise."""
    
    # Locators
    SEARCH_BOX = (By.CSS_SELECTOR, "input[name='search']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button#submit_search")
    PRODUCTS_CONTAINER = (By.CSS_SELECTOR, ".features_items")
    FIRST_PRODUCT_ADD_TO_CART = (By.CSS_SELECTOR, ".features_items:first-child a.add-to-cart")
    FIRST_PRODUCT_VIEW = (By.CSS_SELECTOR, ".features_items:first-child a[href*='/product_details/']")
    SUCCESS_MODAL = (By.CSS_SELECTOR, ".modal-content")
    VIEW_CART_LINK = (By.CSS_SELECTOR, ".modal-content u")
    LOGGED_IN_USER = (By.CSS_SELECTOR, "li:nth-child(10) a")
    CATEGORIES_LIST = (By.CSS_SELECTOR, "#accordian .panel-group")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def search_product(self, product_name):
        """Busca un producto en la barra de búsqueda."""
        logger.info(f"Buscando producto: {product_name}")
        self.send_keys(*self.SEARCH_BOX, product_name)
        self.click(*self.SEARCH_BUTTON)
    
    def add_first_product_to_cart(self):
        """Agrega el primer producto visible al carrito."""
        logger.info("Agregando primer producto al carrito")
        self.click(*self.FIRST_PRODUCT_ADD_TO_CART)
    
    def view_first_product(self):
        """Abre el detalle del primer producto."""
        logger.info("Viendo detalle del primer producto")
        self.click(*self.FIRST_PRODUCT_VIEW)
    
    def is_search_results_displayed(self):
        """Verifica si se muestran resultados de búsqueda."""
        return self.is_element_present(*self.PRODUCTS_CONTAINER)
    
    def is_success_modal_displayed(self):
        """Verifica si aparece el modal de éxito después de agregar al carrito."""
        return self.is_element_present(*self.SUCCESS_MODAL)
    
    def go_to_cart_from_modal(self):
        """Navega al carrito desde el modal de éxito."""
        logger.info("Navegando al carrito desde el modal")
        self.click(*self.VIEW_CART_LINK)
    
    def is_user_logged_in(self):
        """Verifica si el usuario está logueado."""
        return self.is_element_present(*self.LOGGED_IN_USER)