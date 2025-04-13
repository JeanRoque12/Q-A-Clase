import time
import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

# Capacidades del dispositivo/emulador
capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='emulator-5554',
    appPackage='com.android.settings',
    appActivity='.Settings',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        # Establece la conexión con Appium
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        # Cierra el driver después de cada prueba
        if self.driver:
            self.driver.quit()

    def test_navigate_settings(self) -> None:
        # Espera a que la aplicación cargue completamente
        time.sleep(2)

        # Navega hasta el primer cuadro de búsqueda en la aplicación Ajustes
        search_box = self.driver.find_element(
            by=AppiumBy.ID, 
            value="com.android.settings:id/search_action_bar"
        )
        search_box.click()  # Hace clic en el cuadro de búsqueda

        # Espera a que aparezca el verdadero campo de búsqueda
        time.sleep(2)

        # Escribe "App languages" en el cuadro de búsqueda
        real_search_box = self.driver.find_element(
            by=AppiumBy.ID, 
            value="com.google.android.settings.intelligence:id/open_search_view_edit_text"
        )
        real_search_box.send_keys("App languages")
        time.sleep(2)

        # Hace clic en el widget con el texto "App languages"
        app_languages_option = self.driver.find_element(
            by=AppiumBy.XPATH, 
            value='//android.widget.TextView[@text="App languages"]'
        )
        app_languages_option.click()

        # Espera un poco antes de continuar
        time.sleep(2)

        # Hace clic nuevamente en el widget con el texto "App languages"
        app_languages_option_second = self.driver.find_element(
            by=AppiumBy.XPATH, 
            value='//android.widget.TextView[@text="App languages"]'
        )
        app_languages_option_second.click()

        # Espera un poco antes de continuar
        time.sleep(2)

        # Hace clic en el widget con el texto "Calendar"
        calendar_option = self.driver.find_element(
            by=AppiumBy.XPATH, 
            value='//android.widget.TextView[@text="Calendar"]'
        )
        calendar_option.click()

        # Espera un poco antes de continuar
        time.sleep(2)

        # Hace clic en el widget con el texto "Español (España)"
        spanish_option = self.driver.find_element(
            by=AppiumBy.XPATH, 
            value='//android.widget.TextView[@text="Español (España)"]'
        )
        spanish_option.click()
    
    time.sleep(6)

if __name__ == '__main__':
    unittest.main()
