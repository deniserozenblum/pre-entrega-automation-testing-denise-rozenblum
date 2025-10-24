# Pre-entrega Proyecto Final - Automatización de Testing

Este proyecto se centra en implementar una automatización de pruebas para el sitio web de comercio electrónico SauceDemo (https://www.saucedemo.com), utilizando Selenium WebDriver y Python.

## 🎯 Propósito del Proyecto
El objetivo es automatizar los siguientes flujos en la aplicación SauceDemo:
- Login con credenciales válidas.
- Navegación y verificación del catálogo de productos y de elementos esenciales de la interfaz
- Interacción con el carrito de compras (añadir productos y verificar su contenido)

## 🛠️ Tecnologías Utilizadas
- Python: Lenguaje de programación principal
- Pytest: Framework de testing para estructurar y ejecutar pruebas
- Selenium WebDriver: Para la automatización de la interfaz web en el navegador
- Git/GitHub: Para control de versiones y compartir el repositorio
- WebDriver Manager	Gestión automática de los drivers del navegador (ej. ChromeDriver).

## 📁 Estructura del Proyecto

 	pre-entrega-automation-testing-denise-rozenblum 
		├── tests/
		│     ├── test_login.py        # Pruebas relacionadas con el Login
		│     ├── test_inventory.py    # Pruebas de Inventario y Elementos de navegación
		│     └── test_cart.py         # Pruebas de Carrito de Compra y Flujo de Productos
		│
		├── run_tests.py            # Archivo para la ejecución de todos los tests
		├── conftest.py             # Hooks de Pytest, fixtures
		├── report.html             # Reporte HTML final generado por pytest
		├── README.md               # Descripción del proyecto
		└── utils.py                # Funciones reutilizables


## ⚙️ Instalación de Dependencias
Asegurarse de tener Python instalado.
Instala las dependencias necesarias:

	pip install selenium
	pip install pytest
	pip install pytest-html
	pip install webdriver-manager

Asegurarse de que el WebDriver esté en tu PATH o especifica su ubicación en el código.

## ▶️ Ejecución de las Pruebas
Para ejecutar todas las pruebas y generar el reporte HTML:  -m pytest run_tests.py

Al finalizar la ejecución, se genera un reporte HTML con el detalle de:
- Casos ejecutados.
- Resultados (passed/failed).
- Tiempos de ejecución.
- Capturas en caso de error (si corresponde).


## ✅ Funcionalidades Implementadas

- Automatización de Login Caso de éxito con credenciales válidas.
- Verificación de redirección a página de inventario

- Verificación del Catálogo y comprobación del título de la página
- Verificación de presencia de productos visibles
- Validación de elementos de la interfaz (menú, filtros, etc.)

- Interacción con el Carrito 
- Añadir producto al carrito
- Verificar que el contador se incremente
- Navegar al carrito
- Comprobar que el producto añadido aparezca correctamente


👤 **Autora:** Denise Agostina Rozenblum

📝 **Notas:** Este proyecto fue desarrollado como pre-entrega para el curso de Automatización de Testing de Talento Tech. 
