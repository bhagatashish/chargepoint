import pytest
from selenium.webdriver.common.by import By
import time


@pytest.mark.usefixtures('browserinvocation')
class chargePointLinks:
    def __init__ (self, driver):
        self.driver = driver
    findStation_locator = (By.XPATH, "//*[@target='_self']//child::i[1]")
    inputText = (By.XPATH, "//*[@id='search_field']")
    search_Button = (By.XPATH, "//*[@id='searchButton']")
    def findStationLink(self):
        return self.driver.find_element(*chargePointLinks.findStation_locator).click()

    def input_city(self):
        return self.driver.find_element(*chargePointLinks.inputText)

    def searchbutton(self):
        return self.driver.find_element(*chargePointLinks.search_Button).click()

    def wait(self):
        return time.sleep(5)




