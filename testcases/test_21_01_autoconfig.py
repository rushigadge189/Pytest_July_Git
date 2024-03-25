import time

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from utilities.ReadConfig import Readconfig


class Test_21_01_practise_auto():
    Username=Readconfig.getUserName() ;
    Pasword=Readconfig.getPasssWord() ;
    def test_21_01_pautmation(self,setup):

        self.driver=setup ;

        self.driver.get('https://practicetestautomation.com/practice-test-login/');


        self.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(self.Username) ;


        self.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(self.Pasword) ;


        self.driver.find_element(By.XPATH, '//input[@id="username"]').click() ;

        self.driver.find_element(By.XPATH, '//button[text()="Submit"]').click() ;


        if(self.driver.title=='Logged In Successfully | Practice Test Automation') :
            self.driver.save_screenshot('D:\\PYTEST_JULY\\screenshots\\test_21_01_pass.png') ;

            print('\n********LOGIN SUCCESSFUL********') ;

            self.driver.find_element(By.XPATH, '//a[text()="Log out"]').click() ;

            self.driver.close() ;

            assert True ;

        else:
            self.driver.save_screenshot('D:\\PYTEST_JULY\\screenshots\\test_21_01_pass.png');

            print('\n********LOGIN UNSUCCESSFUL*********');

            self.driver.close() ;

            assert False ;

