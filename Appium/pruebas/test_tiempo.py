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
        # Espera a que la aplicación cargue
        time.sleep(2)

        # Usa UiScrollable para hacer scroll hasta "System"
        self.driver.find_element(
            by=AppiumBy.ANDROID_UIAUTOMATOR, 
            value='new UiScrollable(new UiSelector().scrollable(true)).scrollTextIntoView("System")'
        ).click()

        # Espera y luego hace clic en "Date & time"
        time.sleep(2)
        self.driver.find_element(
            by=AppiumBy.ANDROID_UIAUTOMATOR, 
            value='new UiSelector().text("Date & time")'
        ).click()

        # Espera y luego hace clic en "Use location"
        time.sleep(2)
        self.driver.find_element(
            by=AppiumBy.ANDROID_UIAUTOMATOR, 
            value='new UiSelector().text("Use location")'
        ).click()
        
    time.sleep(5)

if __name__ == '__main__':
    unittest.main()
