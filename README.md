# Framework de Automatización de Pruebas - Proyecto Final

## 1. 🎯 Propósito del Proyecto

Este repositorio contiene un **framework de automatización de pruebas integral** desarrollado en Python como trabajo final integrador del curso. El objetivo es validar tanto la **interfaz de usuario (UI)** como los **servicios backend (API)** del sitio [Automation Exercise](https://automationexercise.com), asegurando la calidad del software mediante:

- ✅ Pruebas funcionales de UI con flujos completos de e-commerce
- ✅ Pruebas de API cubriendo métodos GET, POST y DELETE
- ✅ Escenarios positivos y negativos
- ✅ Parametrización con datos externos (JSON)
- ✅ Generación automática de reportes HTML y capturas de pantalla
- ✅ Sistema de logging detallado para facilitar la depuración

El framework está diseñado para ser **escalable, mantenible y reutilizable**, aplicando buenas prácticas de la industria como el patrón **Page Object Model (POM)**.

---

## 2. 🛠️ Tecnologías Utilizadas

| Categoría | Tecnología | Versión | Propósito |
|-----------|------------|---------|-----------|
| **Lenguaje** | Python | 3.x | Lenguaje principal del framework |
| **UI Testing** | Selenium WebDriver | 4.15.2 | Automatización de navegador |
| **API Testing** | Requests | 2.31.0 | Consumo de APIs REST |
| **Framework de Tests** | Pytest | 7.4.3 | Ejecución y organización de tests |
| **Reportes** | pytest-html | 4.1.1 | Generación de reportes HTML |
| **WebDriver Manager** | webdriver-manager | 4.0.1 | Gestión automática de drivers |
| **Patrón de Diseño** | Page Object Model (POM) | - | Separación de responsabilidades |
| **Datos Externos** | JSON | - | Parametrización de tests |

---

## 3. 📂 Estructura del Proyecto
proyecto-final-automation-testing-juliana-londono-leon/
│
├── pages/ # Page Object Model (UI)
│ ├── init.py
│ ├── base_page.py # Clase base con métodos genéricos
│ ├── login_page.py # Página de login
│ ├── home_page.py # Página principal
│ ├── search_page.py # Página de resultados de búsqueda
│ ├── cart_page.py # Página del carrito
│ └── product_page.py # Página de detalle de producto
│
├── tests/ # Casos de prueba
│ ├── ui/ # Pruebas de UI (Selenium)
│ │ ├── test_login.py # Login exitoso y fallido (parametrizado)
│ │ ├── test_search.py # Búsqueda de productos (parametrizado)
│ │ ├── test_cart.py # Agregar al carrito y ver detalle
│ │ └── test_negative_scenarios.py # Escenarios negativos
│ └── api/ # Pruebas de API (Requests)
│ ├── test_get_users.py # Método GET
│ ├── test_post_users.py # Método POST
│ └── test_delete_users.py # Método DELETE
│
├── data/ # Fuentes externas de datos
│ ├── users_data.json # Datos de login/registro
│ ├── search_data.json # Datos de búsqueda
│ └── api_data.json # Datos de pruebas API
│
├── utils/ # Utilidades y configuraciones
│ ├── init.py
│ ├── logger.py # Sistema de logging
│ └── api_client.py # Cliente HTTP encapsulado
│
├── reports/ # Generados automáticamente (NO subir a Git)
│ ├── html/ # Reportes HTML de pytest
│ ├── screenshots/ # Capturas de fallos
│ └── logs/ # Archivos de log
│
├── conftest.py # Fixtures globales y hooks de pytest
├── pytest.ini # Configuración de pytest
├── requirements.txt # Dependencias del proyecto
├── .gitignore # Archivos ignorados por Git
└── README.md # Este archivo


### 🎨 Principios de Diseño Aplicados

- **Page Object Model (POM)**: Separación entre la lógica de los tests y la interacción con las páginas.
- **DRY (Don't Repeat Yourself)**: Métodos reutilizables en `BasePage`.
- **Data-Driven Testing**: Parametrización desde archivos JSON externos.
- **Fail-Fast**: Screenshots automáticos solo cuando un test falla.

---

## 4. 📦 ¿Cómo Instalar las Dependencias?

### Requisitos Previos
- Python 3.8 o superior instalado ([descargar aquí](https://www.python.org/downloads/))
- Git instalado ([descargar aquí](https://git-scm.com/))
- Google Chrome instalado en tu computadora
- pip install -r requirements.txt

### Pasos de Instalación

**1. Clonar el repositorio:**
```bash
git clone https://github.com/zigguratdigitaldesign-design/proyecto-final-automation-testing-juliana-londono-leon.git
cd proyecto-final-automation-testing-juliana-londono-leon

### ¿Cómo Ejecutar las Pruebas?
pytest
## Ejecutar solo pruebas de UI
pytest -m ui -v
## Ejecutar solo pruebas de API
pytest -m api -v
## Ejecutar un archivo específico
pytest tests/ui/test_login.py -v
## Ejecutar con reporte HTML detallado
pytest --html=reports/html/report.html --self-contained-html

