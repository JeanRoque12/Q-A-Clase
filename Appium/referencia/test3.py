import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy as By
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

driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

# Obtener todas las ventanas disponibles
windows = driver.window_handles
print(windows)

# Cambiar a la segunda ventana (la nueva ventana emergente)
driver.switch_to.window(windows[1])

# Realiza las acciones necesarias en la nueva ventana
popup_button = driver.find_element(By.ID, 'popup_button')
popup_button.click()

# Regresar a la ventana principal
driver.switch_to.window(windows[0])


