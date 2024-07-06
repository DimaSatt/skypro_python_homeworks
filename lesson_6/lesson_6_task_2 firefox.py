from selenium import webdriver



firefox = webdriver.Firefox()
try:
   
    firefox.get("http://uitestingplayground.com/textinput")
    button_name = firefox.find_element(
        "id", "newButtonName").send_keys("SkyPro")
    confirm_button_name = firefox.find_element("id","updatingButton").click()
    new_button_name = firefox.find_element("id","updatingButton").text
    print(new_button_name)

except Exception as ex:
        print(ex)
finally:
       firefox.quit()    
