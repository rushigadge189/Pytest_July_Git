import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.logger import LogGenerator


class Test_20_03_logger_heroku():
    log=LogGenerator.loggen() ;
    def test_20_03_heroku(self,setup):
        self.driver=setup ;

        self.log.info('TEST CASE IS STARTED') ;

        self.log.info('OPENING THE BROWSER') ;

        self.log.info('GO TO THE URL') ;

        self.driver.get('https://the-internet.herokuapp.com/login') ;

        self.log.info("ENTERING THE USERNAME") ;
        self.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys('tomsmith') ;

        self.log.info('ENTERING THEPASSWORD') ;
        self.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys('SuperSecretPassword!') ;

        self.log.info('CLICK ON THE LOGIN BUTTON') ;
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click() ;

        self.log.info('CHECKING FOR THE STATUS') ;
        try:
            self.driver.find_element(By.XPATH, '//i[text()=" Logout"]') ;

            self.log.info('TAKING THE SCREENSHOT') ;
            self.driver.save_screenshot('D:\\PYTEST_JULY\\screenshots\\test_20_03_pass.png') ;
            print('\n**********LOGIN SUCCESSFUL**********');

            self.log.info('CLICK ON THE LOGOUT BUTON') ;
            self.driver.find_element(By.XPATH, '//i[text()=" Logout"]').click();

            self.log.info('TEST CASE IS PASSED') ;
            assert True ;

        except:

            self.log.info('TAKING THE SCREENSHOT') ;
            self.driver.save_screenshot('D:\\PYTEST_JULY\\screenshots\\test_20_03_fail.png');
            print('\n**********LOGIN UNSUCCESSFUL**********');

            self.log.info('TEST CASE IS FAILED') ;
            assert False ;

        self.log.info('CLOSING THE BROWSER') ;
        self.driver.close() ;

        self.log.info('TEST CASE IS COMPLETED') ;

