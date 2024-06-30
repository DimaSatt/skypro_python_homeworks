from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

try:
    #chrome.maximize_window(), или firefox.maximize_window()
    chrome.get("https://the-internet.herokuapp.com/login")
    firefox.get("https://the-internet.herokuapp.com/login")  
    input_name = chrome.find_element(By.ID, "username") .send_keys("DimaS")
    input_name = firefox.find_element(By.ID, "username") .send_keys("DimaS")
    sleep(3)
    #input_name.send_keys("DimaS")
    input_pass = chrome.find_element(
        By.ID, "password").send_keys("SuperSecret")
    input_pass = firefox.find_element(
         By.ID, "password").send_keys("SuperSecret")
    sleep(3)
    #input_pass.send_keys("SuperSecret")
    button = chrome.find_element(By.TAG_NAME,"button").click()
    button = firefox.find_element(By.TAG_NAME,"button").click()
    sleep(2)

except Exception as ex:
        print(ex)
finally:
   
    chrome.quit()
    firefox.quit()