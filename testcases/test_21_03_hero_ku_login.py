import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.ReadConfig import Readconfig

class Test_21_03_heroku() :
    username123=Readconfig.getUserName() ;
    password123=Readconfig.getPassWord() ;
    def test_21_03_hero_ku(self,setup):

        self.driver=setup ;

        self.driver.get('https://the-internet.herokuapp.com/login') ;

        try:
            self.driver.save_screenshot('D:\\PYTEST_JULY\screenshots\\test_21_03_pass.png') ;

            self.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(self.username123) ;

            self.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(self.password123) ;

            self.driver.find_element(By.XPATH, '//button[@type="submit"]').click() ;

            self.driver.find_element(By.XPATH, '//i[text()=" Logout"]').click();

            self.driver.close();
            assert True ;
        except:
            self.driver.save_screenshot('D:\\PYTEST_JULY\\screenshots\\test_21_03_fail.png') ;
            print('********TEST CASE IS FAILED*********') ;
            self.driver.close();
            assert False ;