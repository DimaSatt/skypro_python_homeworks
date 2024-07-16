from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

chrome = webdriver.Chrome()

try:
    chrome.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    chrome.find_element(By.NAME, "first-name").send_keys("Иван")
    chrome.find_element(By.NAME, "last-name").send_keys("Пертов")
    chrome.find_element(By.NAME, "address").send_keys("Ленинв 5-33")
    chrome.find_element(By.NAME, "zip-code").send_keys("")
    chrome.find_element(By.NAME, "city").send_keys("москва")
    chrome.find_element(By.NAME, "country").send_keys("Россия")
    chrome.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    chrome.find_element(By.NAME, "phone").send_keys("+79062222222")
    chrome.find_element(By.NAME, "job-position").send_keys("QA")
    chrome.find_element(By.NAME, "company").send_keys("SkyPro")
    sleep(2)
    #WebDriverWait(chrome,40, 0.1).until(EC((By.TAG_NAME, "button"))).click()
    button = chrome.find_element(By.TAG_NAME,"button").click()
    sleep(2)   
    #Проверка подсветки полей
    assert "danger" in chrome.find_element(By.ID, "zip_cpde").get_atribute("class") 
    assert "success" in chrome.find_element(By.ID, "first-name").get_atribute("class")
    assert "success" in chrome.find_element(By.ID, "last-name").get_atribute("class")
    assert "success" in chrome.find_element(By.ID, "address").get_atribute("class")
    assert "success" in chrome.find_element(By.ID, "city").get_atribute("class")
    assert "success" in chrome.find_element(By.ID, "country").get_atribute("class")
    assert "success" in chrome.find_element(By.ID, "e-mail").get_atribute("class")
    assert "success" in chrome.find_element(By.ID, "phone").get_atribute("class")
    assert "success" in chrome.find_element(By.ID, "job-position").get_atribute("class")
    assert "success" in chrome.find_element(By.ID, "company").get_atribute("class")
    
except Exception as ex:
        print(ex)
finally:
    chrome.quit()