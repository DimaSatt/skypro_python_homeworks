from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


firefox = webdriver.Firefox()
wait = WebDriverWait(firefox,40,0.1)
try:

    
    firefox.get("http://uitestingplayground.com/ajax")
    blue_button = firefox.find_element(By.CSS_SELECTOR, "#ajaxButton").click()
    text_from_content = wait.until(EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, ".bg-success"))).text
    print(text_from_content)
except Exception as ex:
        print(ex)
finally:
    firefox.quit()