import time

from selenium import webdriver
from pageobjects.test_18_02_swaglabspages import Test_18_02_swag

class Test_18_02_swaglabdemo():
    def test_18_swaglabs(self,setup):

        self.driver=setup ;

        self.obj=Test_18_02_swag(self.driver) ;

        self.obj.test_open_page('https://www.saucedemo.com/') ;

        self.obj.test_enter_username('problem_user');

        self.obj.test_enter_password('secret_sauce') ;

        self.obj.test_login_click();

        if(self.obj.test_status()==True) :
            self.driver.save_screenshot("D:\\PYTEST_JULY\\screenshots\\test_18_02_swaglabs_pass.png") ;
            print('\nLOGIN SUCCESSFUL........!') ;
        else:
            self.driver.save_screenshot("D:\\PYTEST_JULY\\screenshots\\test_18_02_swaglabs_fail.png");
            print('\nLOGIN UNSUCCESSFUL........!');

        self.obj.test_burger_click() ;

        self.obj.test_logout_click();

        self.driver.close() ;





