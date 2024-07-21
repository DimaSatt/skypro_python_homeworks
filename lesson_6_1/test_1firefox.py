
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from configuration import *
from time import sleep



def test_data_types(firefox_browser):
    firefox_browser.get(URL_1)
    firefox_browser.find_element(By.NAME, "first-name").send_keys("Иван")
    firefox_browser.find_element(By.NAME, "last-name").send_keys("Пертов")
    firefox_browser.find_element(By.NAME, "address").send_keys("Ленинв 5-33")
    firefox_browser.find_element(By.NAME, "zip-code").send_keys("")
    firefox_browser.find_element(By.NAME, "city").send_keys("москва")
    firefox_browser.find_element(By.NAME, "country").send_keys("Россия")
    firefox_browser.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    firefox_browser.find_element(By.NAME, "phone").send_keys("+79062222222")
    firefox_browser.find_element(By.NAME, "job-position").send_keys("QA")
    firefox_browser.find_element(By.NAME, "company").send_keys("SkyPro")
    sleep(2)
    WebDriverWait(firefox_browser,40, 0.1).until(EC.element_to_be_clickable((By.TAG_NAME, "button"))).click()
    sleep(2)   
    #Проверка подсветки полей
    assert "danger" in firefox_browser.find_element(By.ID, "zip-code").get_attribute("class") 
    assert "success" in firefox_browser.find_element(By.ID, "first-name").get_attribute("class")
    assert "success" in firefox_browser.find_element(By.ID, "last-name").get_attribute("class")
    assert "success" in firefox_browser.find_element(By.ID, "address").get_attribute("class")
    assert "success" in firefox_browser.find_element(By.ID, "city").get_attribute("class")
    assert "success" in firefox_browser.find_element(By.ID, "country").get_attribute("class") 
    assert "success" in firefox_browser.find_element(By.ID, "e-mail").get_attribute("class")
    assert "success" in firefox_browser.find_element(By.ID, "phone").get_attribute("class")
    assert "success" in firefox_browser.find_element(By.ID, "job-position").get_attribute("class")
    assert "success" in firefox_browser.find_element(By.ID, "company").get_attribute("class")
    
    