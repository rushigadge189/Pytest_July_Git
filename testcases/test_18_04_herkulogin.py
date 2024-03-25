import time

from selenium import webdriver
from pageobjects.test_18_04_herokupages import Test_18_herkoku

class Test_18_04_heroku_internet():

    def test_18_04_hk(self,setup):
        self.driver=setup ;

        self.obj=Test_18_herkoku(self.driver) ;

        self.obj.test_enter_url('https://the-internet.herokuapp.com/login') ;

        self.obj.test_enter_username('tomsmith') ;

        self.obj.test_enter_password('SuperSecretPassword!') ;

        self.obj.test_login_click();

        self.obj.test_print_text();

        if(self.obj.test_status()==True) :
            self.driver.save_screenshot("D:\\PYTEST_JULY\\screenshots\\test_18_04_pass.png") ;
            print('\nLOGIN SUCCESSFUL.......!') ;

        else:
            self.driver.save_screenshot("D:\\PYTEST_JULY\\screenshots\\test_18_04_fail.png");
            print('\nLOGIN UNSUCCESSFUL.......!');

        self.obj.test_logout_click() ;

        self.driver.close();


