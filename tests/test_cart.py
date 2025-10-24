from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_cart_functionality(login_in_driver):
    try:
        driver = login_in_driver

        # Obtener el nombre del primer producto para validarlo después
        product_name_element = driver.find_element(By.CLASS_NAME, "inventory_item_name")
        product_name = product_name_element.text
        print(f"Producto seleccionado: {product_name}")
        
        # Añadir el primer producto al carrito
        driver.find_element(By.XPATH, "//button[contains(@data-test, 'add-to-cart')]").click()
        
        # Esperar y verificar que aparezca el badge del carrito de compras 
        badge = WebDriverWait(driver, 10).until( EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")) )
        # Verificar que el contador del carrito muestra 1 
        assert badge.text == "1", f"El contador del carrito debería mostrar 1, pero muestra {badge.text}" 
        print("✅ Producto añadido al carrito correctamente!") 
        
        # Navegar al carrito
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        
        # Verificar que estamos en la página del carrito
        WebDriverWait(driver, 10).until(
            EC.url_contains("cart.html")
        )
        assert "/cart.html" in driver.current_url, "No se Redirigio al carrito"
        
        # Verificar que el producto añadido aparezca en el carrito
        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(cart_items) == 1, f"Debería haber 1 producto en el carrito, pero hay {len(cart_items)}"
        
        # Verificar que sea el mismo producto que añadimos
        cart_item_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        assert cart_item_name == product_name, f"El producto en el carrito ({cart_item_name}) no coincide con el añadido ({product_name})"
        
        print("✅ Verificación del carrito completada")

    except Exception as e:
        print(f"Error en test_cart:{e}")
        raise
    
    finally:
        driver.quit()