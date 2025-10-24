from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login_validation(login_in_driver):
    try:
        driver = login_in_driver

        # Verificar que estamos en la página de inventario
        assert "/inventory.html" in driver.current_url, "No se redirigio correctamente al inventario"

        # Verificar título de sección 
        titulo = driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title').text
        assert titulo == 'Products'

    except Exception as e:
        print(f"Error en test_login:{e}")
        raise
    
    finally:
        driver.quit()