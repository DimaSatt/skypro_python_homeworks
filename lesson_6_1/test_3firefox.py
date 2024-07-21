from selenium.webdriver.common.by import By
from configuration import *

def test_shop_form(firefox_browser):
    firefox_browser.get(URL_3)
    firefox_browser.find_element(By.ID, "user-name").send_keys("standard_user")
    firefox_browser.find_element(By.ID, "password").send_keys("secret_sauce")
    firefox_browser.find_element(By.ID, "login-button").click()
    firefox_browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    firefox_browser.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    firefox_browser.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    firefox_browser.find_element(By.ID, "shopping_cart_container").click()
    firefox_browser.find_element(By.ID, "checkout").click()
    firefox_browser.find_element(By.ID, "first-name").send_keys("Dima")
    firefox_browser.find_element(By.ID, "last-name").send_keys("Sattarov")
    firefox_browser.find_element(By.ID, "postal-code").send_keys("601500")
    firefox_browser.find_element(By.ID, "continue").click()
    total_price = firefox_browser.find_element(By.CLASS_NAME, 'summary_total_label')
    total = total_price.text.strip().replace("Total: $", "")

    expected_total = "58.29"
    assert total == expected_total #Проверяем что итоговая сумма 58,29
    print(f"Итоговая сумма равна ${total}") #Выводим сообщениев случае успешного выполнения