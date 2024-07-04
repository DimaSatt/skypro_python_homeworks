from selenium import webdriver


chrome = webdriver.Chrome()
firefox = webdriver.Firefox()
try:
    chrome.get("http://uitestingplayground.com/textinput")
    firefox.get("http://uitestingplayground.com/textinput")
    button_name = chrome.find_element(
        "id", "newButtonName").send_keys("SkyPro")
    confirm_button_name = chrome.find_element("id","updatingButton").click()
    new_button_name = chrome.find_element("id","updatingButton").text
    button_name = firefox.find_element(
        "id", "newButtonName").send_keys("SkyPro")
    confirm_button_name = firefox.find_element("id","updatingButton").click()
    new_button_name = firefox.find_element("id","updatingButton").text
    print(new_button_name)

except Exception as ex:
        print(ex)
finally:
    chrome.quit()
    firefox.quit()    
