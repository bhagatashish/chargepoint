import time
from ChargePointFramework.pageObjectModel.chargePointlinks import chargePointLinks
from ChargePointFramework.utitlities.baseClass import baseClass


class Teste2e(baseClass):
    def test_homePage(self):
        chargePoint_links = chargePointLinks(self.driver)
        chargePoint_links.findStationLink()
        chargePoint_links.input_city().send_keys('mexico')
        chargePoint_links.input_city().click()
        time.sleep(3)
        chargePoint_links.searchbutton()