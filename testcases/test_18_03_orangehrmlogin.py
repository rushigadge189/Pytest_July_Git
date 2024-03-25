import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageobjects.test_18_03_oranhehrm_pages import Test_18_OHRM

class Test_18_02_orhm_login():
    def test_orangehrm(self,setup):

        self.driver=setup;

        self.obj=Test_18_OHRM(self.driver) ;

        self.obj.test_enter_url('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login') ;

        self.obj.test_enter_username('Admin');

        self.obj.test_enter_password('admin123');

        self.obj.test_click_login() ;

        self.wait=WebDriverWait(self.driver,10) ;

        if(self.obj.test_status()==True) :
            self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//span[@title="Engineering"]')))
            self.driver.save_screenshot("D:\\PYTEST_JULY\\screenshots\\test_18_03_pass.png") ;
            print('\nLOGIN SUCCESSFUL.......!') ;
        else:
            self.driver.save_screenshot("D:\\PYTEST_JULY\\screenshots\\test_18_03_fail.png") ;
            print('\nLOGIN UNSUCESSFUL.......!') ;

        self.obj.test_click_menu() ;

        self.obj.test_click_logout();

        self.driver.close();