from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login():
    driver = webdriver.Chrome()
    driver.get("https://www.demoblaze.com")

    driver.find_element(By.ID, "login2").click()
    
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "logInModal")))

    driver.find_element(By.ID, "Manny111").send_keys("testuser")
    driver.find_element(By.ID, "password123").send_keys("password123")
    driver.find_element(By.XPATH, "//button[text()='Log in']").click()
    
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "nameofuser")))

    assert "Welcome testuser" in driver.page_source

    driver.quit()

if __name__ == "__main__":
    test_login()
