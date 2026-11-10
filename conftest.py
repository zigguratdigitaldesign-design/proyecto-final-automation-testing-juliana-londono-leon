import pytest
import logging
from datetime import datetime
from selenium import webdriver
from utils.logger import setup_logger

# Configurar el logger global
logger = setup_logger()

@pytest.fixture(scope="function")
def setup_ui(request):
    """Fixture para inicializar y cerrar el navegador en pruebas UI."""
    logger.info("Iniciando navegador para la prueba UI")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    
    # Yield devuelve el driver al test
    yield driver 
    
    logger.info("Cerrando navegador")
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook de Pytest para capturar screenshot AUTOMÁTICO solo si el test falla.
    """
    outcome = yield
    rep = outcome.get_result()
    
    # Solo actuamos si el test es de UI y ha fallado
    if rep.when == "call" and rep.failed and "setup_ui" in item.fixturenames:
        try:
            driver = item.funcargs["setup_ui"]
            
            # Formato de fecha y hora
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            # Nombre descriptivo: nombre_del_test_FechaHora.png
            screenshot_name = f"reports/screenshots/{item.name}_{timestamp}.png"
            
            driver.save_screenshot(screenshot_name)
            logger.error(f"Test fallido. Screenshot guardado en: {screenshot_name}")
            
            # Adjuntar el screenshot al reporte HTML de pytest
            pytest_html = item.config.pluginmanager.getplugin("html")
            if pytest_html:
                with open(screenshot_name, 'rb') as image_file:
                    import base64
                    encoded = base64.b64encode(image_file.read()).decode('utf-8')
                    pytest_html.extras.image(encoded, mime_type='image/png')
                    
        except Exception as e:
            logger.error(f"No se pudo capturar el screenshot: {e}")