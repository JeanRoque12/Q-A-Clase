from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_purchase():
    driver = webdriver.Chrome()
    driver.get("https://www.demoblaze.com")

    driver.find_element(By.ID, "cartur").click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Products']")))

    driver.find_element(By.XPATH, "//button[text()='Place Order']").click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "orderModal")))

    driver.find_element(By.ID, "name").send_keys("Juan Pérez")
    driver.find_element(By.ID, "country").send_keys("México")
    driver.find_element(By.ID, "city").send_keys("CDMX")
    driver.find_element(By.ID, "card").send_keys("1234-5678-9012-3456")
    driver.find_element(By.ID, "month").send_keys("12")
    driver.find_element(By.ID, "year").send_keys("2026")

    driver.find_element(By.XPATH, "//button[text()='Purchase']").click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Thank you for your purchase!']")))

    assert "Thank you for your purchase!" in driver.page_source

    driver.quit()

if __name__ == "__main__":
    test_purchase()
