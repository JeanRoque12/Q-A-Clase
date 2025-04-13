import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.keys import Keys  # Importa las teclas para emular Enter
import time

# Configuración de las capacidades
capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='emulator-5554',  # Dispositivo AVD
    appPackage='com.google.android.apps.nexuslauncher',  # Paquete para el launcher de Android
    appActivity='com.google.android.apps.nexuslauncher.NexusLauncherActivity',  # Actividad del launcher
    language='en',
    locale='US'
)

# Dirección del servidor de Appium
appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        # Inicializa la conexión con Appium usando las capacidades configuradas
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        # Cierra la conexión con Appium después de cada prueba
        if self.driver:
            self.driver.quit()

    def test_search_in_chrome(self) -> None:
        # Espera a que la pantalla de inicio cargue
        time.sleep(5)

        # Encuentra el ícono de Chrome por su texto "Chrome" en el launcher
        chrome_icon = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Chrome"]')

        # Haz clic en el ícono de Chrome
        chrome_icon.click()

        # Espera a que Chrome se inicie
        time.sleep(5)

        # Encuentra el search box en Chrome usando su ID
        search_box = self.driver.find_element(by=AppiumBy.ID, value='com.android.chrome:id/search_box_text')

        # Escribe "gato" en el search box
        search_box.send_keys("gato")

        # Emula presionar la tecla Enter para buscar
        self.driver.press_keycode(66)

        # Espera un momento para que los resultados de búsqueda carguen
        time.sleep(5)

if __name__ == '__main__':
    unittest.main()
