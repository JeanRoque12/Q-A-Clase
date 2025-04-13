import time
import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

# Capacidades necesarias para la conexión con el dispositivo/emulador
capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='emulator-5554',  # Cambié el deviceName aquí
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

    def test_adjust_brightness(self) -> None:
        # Espera que la aplicación cargue completamente
        time.sleep(2)

        # Navega hasta el primer cuadro de búsqueda en la aplicación Ajustes
        search_box = self.driver.find_element(by=AppiumBy.ID, value="com.android.settings:id/search_action_bar")
        search_box.click()  # Hace clic en el cuadro de búsqueda

        # Espera a que aparezca el verdadero campo de búsqueda
        time.sleep(2)

        # Escribe "Brightness" en el cuadro de búsqueda verdadero
        real_search_box = self.driver.find_element(by=AppiumBy.ID, value="com.google.android.settings.intelligence:id/open_search_view_edit_text")
        real_search_box.send_keys("Brightness")
        time.sleep(2)

        # Hace clic en la opción "Brightness level" utilizando el texto
        brightness_option = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Brightness level"]')
        brightness_option.click()

        # Espera a que aparezca la nueva sección
        time.sleep(2)

        # Hace clic en el segundo botón "Brightness level" utilizando el texto (en la nueva sección)
        brightness_option_second = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Brightness level"]')
        brightness_option_second.click()

        # Espera a que aparezca el control deslizante (slider)
        time.sleep(2)

        # Selecciona el slider utilizando el ID o XPath
        slider = self.driver.find_element(
            by=AppiumBy.XPATH, 
            value='//android.widget.SeekBar[@resource-id="com.android.systemui:id/slider"]'
        )

        # Realiza el gesto de deslizamiento (swipe) utilizando 'mobile: swipeGesture'
        self.driver.execute_script('mobile: swipeGesture', {
            'elementId': slider.id,
            'direction': 'right',  # o 'right', según la dirección deseada
            'percent': 0.75       # Desliza el 75% del slider
        })

        time.sleep(2)  # Espera para asegurar que el cambio se haya realizado

        # Obtener el tamaño de la pantalla
        screen_size = self.driver.get_window_size()
        screen_width = screen_size['width']
        screen_height = screen_size['height']

        # Calcular las coordenadas para hacer clic en el centro de la pantalla
        center_x = screen_width // 2
        center_y = screen_height // 2

        # Realizar un clic en el centro de la pantalla
        self.driver.tap([(center_x, center_y)])

        time.sleep(5)  # Espera para asegurar que el clic se haya realizado

if __name__ == '__main__':
    unittest.main()
