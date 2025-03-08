from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_add_to_cart():
    driver = webdriver.Chrome()
    driver.get("https://www.demoblaze.com")

    # Esperar que la página cargue
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Laptops")))

    # Seleccionar la categoría de Laptops
    driver.find_element(By.LINK_TEXT, "Laptops").click()

    # Esperar que se carguen los productos
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Sony vaio i5")))

    # Seleccionar el producto
    driver.find_element(By.LINK_TEXT, "Sony vaio i5").click()

    # Esperar que se cargue la página del producto
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Sony vaio i5']")))

    # Hacer clic en "Add to cart"
    driver.find_element(By.XPATH, "//a[text()='Add to cart']").click()

    # Esperar la alerta y aceptarla
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("Alerta mostrada:", alert.text)  # Verificar el mensaje de la alerta
    alert.accept()

    # Ir al carrito
    driver.find_element(By.ID, "cartur").click()

    # Esperar que se cargue la página del carrito
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Products']")))

    # Verificar si el producto está en el carrito
    try:
        product_in_cart = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//td[text()='Sony vaio i5']"))
        )
        print("✅ Producto encontrado en el carrito: Sony vaio i5")
    except:
        print("❌ ERROR: El producto no se encuentra en el carrito.")

    # Esperar unos segundos para verificar visualmente
    time.sleep(3)

    driver.quit()

if __name__ == "__main__":
    test_add_to_cart()
