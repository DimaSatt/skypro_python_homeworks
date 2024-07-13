from selenium.webdriver.common.by import By
from configuration import *

def test_shop_form(chrome_browser):
    chrome_browser.get(URL_3)
    chrome_browser.find_element(By.ID, "user_name").send_keys("standart_user")
    chrome_browser.find_element(By.ID, "password").send_keys("secret_sauce")
    chrome_browser.find_element(By.ID, "login_button").click()
    chrome_browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    chrome_browser.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    chrome_browser.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    chrome_browser.find_element(By.ID, "shopping_cart_container").click()
    chrome_browser.find_element(By.ID, "first_name").send_keys("Dima")
    chrome_browser.find_element(By.ID, "last_name").send_keys("Sattarov")
    chrome_browser.find_element(By.ID, "postal-code").send_keys("601500")
    chrome_browser.find_element(By.ID, "continue").click()
    total_prise = chrome_browser.find_element(By.CLASS_NAME, 'summary_total_label')
    total = total_prise.text.strip().replace("Total: $", "")

    expected_total = "58,29"
    assert total == expected_total #Проверяем что итоговая сумма 58,29
    print("Итоговая сумма равна $58,29") #Выводим сообщениев случае успешного выполнения