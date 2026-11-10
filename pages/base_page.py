from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.logger import setup_logger

logger = setup_logger()

class BasePage:
    """Clase base para todos los Page Objects."""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def find_element(self, by, locator):
        """Encuentra un elemento con wait explícito."""
        logger.debug(f"Buscando elemento: {by}={locator}")
        return self.wait.until(EC.presence_of_element_located((by, locator)))
    
    def click(self, by, locator):
        """Click en un elemento esperando que sea clickeable."""
        logger.info(f"Click en: {locator}")
        element = self.wait.until(EC.element_to_be_clickable((by, locator)))
        element.click()
    
    def send_keys(self, by, locator, text):
        """Escribe texto en un campo."""
        logger.info(f"Escribiendo en {locator}: {text}")
        element = self.find_element(by, locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, by, locator):
        """Obtiene el texto de un elemento."""
        element = self.find_element(by, locator)
        text = element.text
        logger.debug(f"Texto obtenido de {locator}: {text}")
        return text
    
    def is_element_present(self, by, locator, timeout=5):
        """Verifica si un elemento está presente."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, locator))
            )
            return True
        except:
            return False
        