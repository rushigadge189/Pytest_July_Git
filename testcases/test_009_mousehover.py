import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Test_009_mouse_hover():
    def test_009(self):

        driver=webdriver.Chrome();

        driver.implicitly_wait(5) ;

        driver.maximize_window();

        driver.get('https://www.google.co.in') ;

        driver.find_element(By.XPATH, '//textarea[@class="gLFyf"]').send_keys('vtiger') ;

        driver.find_element(By.XPATH, '(//input[@class="gNO89b"])[1]').click() ;

        driver.find_element(By.XPATH, '(//h3[@class="LC20lb MBeuO DKV0Md"])[1]').click();

        action=ActionChains(driver) ;

        resource_tab=driver.find_element(By.XPATH, '(//a[@id="navbarPages"])[2]') ;
        action.move_to_element(resource_tab).perform() ;

        driver.save_screenshot("D:\\PYTEST_JULY\\screenshots\\test_009_hover.png") ;

        driver.find_element(By.XPATH, "//div[@class='col-4 p-lg-5']//a[@class='list-link'][normalize-space()='Contact Us']").click() ;

        loc=driver.find_element(By.XPATH,'(//div[@class="col-12 col-md-4 border-left border-dark mb-4 pl-3 py-2 lift"])[2]').text ;
        print('\n***********************\n')
        print(loc) ;

        driver.close() ;