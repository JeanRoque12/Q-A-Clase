from selenium import webdriver
import time

# Iniciar el WebDriver
driver = webdriver.Chrome()
driver.get("https://example.com")

# Agregar una cookie manualmente
cookie = {"name": "session_id", "value": "123456"}
driver.add_cookie(cookie)

# Obtener todas las cookies
cookies = driver.get_cookies()
print("Cookies actuales:", cookies)

# Cerrar el navegador y volver a abrirlo
driver.quit()
driver = webdriver.Chrome()
driver.get("https://example.com")

# Cargar las cookies guardadas
for c in cookies:
    driver.add_cookie(c)

# Refrescar la página para aplicar las cookies
driver.refresh()
time.sleep(2)

driver.quit()

