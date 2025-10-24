from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_inventory(login_in_driver):
    try:
        driver = login_in_driver

        # Verificar el título de la página
        assert driver.title == "Swag Labs", f"El título de la página es incorrecto: {driver.title}"

        # Verificar que existan productos visibles
        products = driver.find_elements(By.CLASS_NAME, "inventory_item")

        assert len(products) > 0, "No hay productos visibles en la pagina"

        # Tomar el primer producto
        primer_producto = products[0]

        # Obtener nombre y precio
        nombre = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
        precio = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text

        print(f"Primer producto encontrado:")
        print(f"Nombre: {nombre}")
        print(f"Precio: {precio}")
    
        #Verificar elementos importantes de la interfaz
        # Validar que los elementos importantes estén presentes y visibles
        wait = WebDriverWait(driver, 10)
        
        filtro = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product_sort_container")))
        menu = wait.until(EC.visibility_of_element_located((By.ID, "react-burger-menu-btn")))
        carrito = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_link")))

        # Comprobar que realmente están visibles
        assert filtro.is_displayed(), "Filtro de productos no encontrado"
        assert menu.is_displayed(), "Menú hamburguesa no encontrado"
        assert carrito.is_displayed(), "Ícono del carrito no encontrado."

    except Exception as e:
        print(f"Error en test_inventory:{e}")
        raise
    
    finally:
        driver.quit()
