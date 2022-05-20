import pytest as pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def browserinvocation(request):
     print("hadkjha")
     driver = webdriver.Chrome(executable_path="C:\\Users\\bhaga\\Desktop\\ashish project\\chromedriver.exe")
     driver.get("https://na.chargepoint.com/")
     driver.maximize_window()
     request.cls.driver= driver

     driver.close()




