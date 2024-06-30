# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.ui import expected_conditions as EC
# from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

try:
    #driwer.maximize_window()
    chrome.get("https://the-internet.herokuapp.com/entry_ad")
    firefox.get("https://the-internet.herokuapp.com/entry_ad")
    #Ждём пока модальное окно не появится и кнопка CIOSE станет кликабельной
    wait = WebDriverWait(chrome,firefox,10)
   
    # modal_window = wait.until(
    #     EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal")))
    close_button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".modal-footer")))
    time.sleep(3)
    #Нажмите кнопку CLOSE в модальном окне
    close_button.click()
    time.sleep(2)

except Exception as ex:
        print(ex)
finally:
    chrome.quit()
    firefox.quit()
    