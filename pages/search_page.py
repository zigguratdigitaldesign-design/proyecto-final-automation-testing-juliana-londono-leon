from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import setup_logger

logger = setup_logger()

class SearchPage(BasePage):
    """Page Object para la página de resultados de búsqueda."""
    
    # Locators
    SEARCHED_ITEMS = (By.CSS_SELECTOR, ".features_items")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".productinfo h2")
    NO_RESULTS_MESSAGE = (By.CSS_SELECTOR, ".features_items p")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def get_search_results_count(self):
        """Obtiene la cantidad de productos encontrados."""
        elements = self.driver.find_elements(*self.SEARCHED_ITEMS)
        count = len(elements)
        logger.info(f"Productos encontrados: {count}")
        return count
    
    def get_first_product_title(self):
        """Obtiene el título del primer producto encontrado."""
        title = self.get_text(*self.PRODUCT_TITLE)
        logger.info(f"Primer producto: {title}")
        return title
    
    def are_results_displayed(self):
        """Verifica si hay resultados de búsqueda."""
        return self.is_element_present(*self.SEARCHED_ITEMS)
    
    def is_no_results_message_displayed(self):
        """Verifica si aparece el mensaje de 'no resultados'."""
        return self.is_element_present(*self.NO_RESULTS_MESSAGE)