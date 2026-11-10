import requests
from utils.logger import setup_logger

logger = setup_logger()

class APIClient:
    """Cliente base para realizar peticiones HTTP a la API."""
    
    def __init__(self, base_url="https://reqres.in"):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })
    
    def get(self, endpoint, params=None):
        """Realiza una petición GET."""
        url = f"{self.base_url}{endpoint}"
        logger.info(f"GET {url} | Params: {params}")
        
        response = self.session.get(url, params=params)
        
        logger.info(f"Respuesta: Status {response.status_code}")
        logger.debug(f"Body: {response.json()}")
        
        return response
    
    def post(self, endpoint, data=None):
        """Realiza una petición POST."""
        url = f"{self.base_url}{endpoint}"
        logger.info(f"POST {url} | Data: {data}")
        
        response = self.session.post(url, json=data)
        
        logger.info(f"Respuesta: Status {response.status_code}")
        logger.debug(f"Body: {response.json()}")
        
        return response
    
    def put(self, endpoint, data=None):
        """Realiza una petición PUT."""
        url = f"{self.base_url}{endpoint}"
        logger.info(f"PUT {url} | Data: {data}")
        
        response = self.session.put(url, json=data)
        
        logger.info(f"Respuesta: Status {response.status_code}")
        logger.debug(f"Body: {response.json()}")
        
        return response
    
    def delete(self, endpoint):
        """Realiza una petición DELETE."""
        url = f"{self.base_url}{endpoint}"
        logger.info(f"DELETE {url}")
        
        response = self.session.delete(url)
        
        logger.info(f"Respuesta: Status {response.status_code}")
        
        return response