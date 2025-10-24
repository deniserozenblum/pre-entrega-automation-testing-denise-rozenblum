from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def login(driver):
    # Abrir la página de login
    driver.get("https://www.saucedemo.com/")

    # Esperar a que el formulario de login sea visible
    username_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    
    # Ingresar credenciales válidas

    username_input.send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
   
    # Hacer clic en el botón de login
    driver.find_element(By.ID, "login-button").click()

    # Verificar login exitoso comprobando la URL
    WebDriverWait(driver, 10).until(EC.url_contains("inventory.html")
    )

