import logging
import os
from datetime import datetime

def setup_logger():
    """Configura el logger global con archivo y consola."""
    # Crear carpeta de logs si no existe
    os.makedirs('reports/logs', exist_ok=True)
    
    logger = logging.getLogger('AutomationFramework')
    logger.setLevel(logging.DEBUG)
    
    # Formato del log
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Handler para archivo (con fecha en el nombre)
    log_filename = f"reports/logs/execution_{datetime.now().strftime('%Y%m%d')}.log"
    file_handler = logging.FileHandler(log_filename, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    
    # Handler para consola
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    
    # Agregar handlers al logger
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    
    return logger