from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import setup_logger

logger = setup_logger()

class LoginPage(BasePage):
    """Page Object para la página de Login de Automation Exercise."""
    
    # Locators
    LOGIN_EMAIL = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    LOGIN_ERROR_MESSAGE = (By.CSS_SELECTOR, "p[style='color: red;']")
    NEW_USER_SIGNUP_BUTTON = (By.CSS_SELECTOR, "a[href='/login']")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://automationexercise.com/login"
    
    def navigate(self):
        """Navega a la página de login."""
        logger.info(f"Navegando a: {self.url}")
        self.driver.get(self.url)
    
    def login(self, email, password):
        """Realiza el login con las credenciales proporcionadas."""
        logger.info(f"Intentando login con email: {email}")
        self.send_keys(*self.LOGIN_EMAIL, email)
        self.send_keys(*self.LOGIN_PASSWORD, password)
        self.click(*self.LOGIN_BUTTON)
    
    def get_error_message(self):
        """Obtiene el mensaje de error de login."""
        return self.get_text(*self.LOGIN_ERROR_MESSAGE)
    
    def is_login_successful(self):
        """Verifica si el login fue exitoso (redirige a home)."""
        return "automationexercise.com" in self.driver.current_url and "/login" not in self.driver.current_url