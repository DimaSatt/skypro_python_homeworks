import pytest
from selenium import webdriver

@pytest.fixture()
def chrome_browser():
    chrome = webdriver.Chrome()
    yield chrome
    chrome.quit()