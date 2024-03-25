from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.logger import LogGenerator
class Test_20_02_swag_labs():
    log=LogGenerator.loggen() ;
    def test_20_02_swaglabs(self,setup):
        self.driver=setup;

        self.log.info('TEST CASE IS STARTED')

        self.log.info('OPENING THE BROWSER') ;

        self.log.info('NAVIGTE TO THE URL') ;

        self.driver.get("https://www.saucedemo.com/") ;

        self.log.info('ENTERING THE USERNAME') ;
        self.driver.find_element(By.XPATH, '//input[@id="user-name"]').send_keys('problem_user') ;

        self.log.info('ENTERING PASSWORD') ;
        self.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys('secret_sauce') ;

        self.log.info('CLICK ON THE LOGIN BUTTON') ;
        self.driver.find_element(By.XPATH, '//input[@type="submit"]').click();

        try:
            self.log.info('CHECKING FOR THE STATUS') ;
            self.driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]');

            self.log.info('TAKING THE SCREENSHOT') ;
            self.driver.save_screenshot('D:\\PYTEST_JULY\\screenshots\\test_20_02_pass.png');

            self.log.info('CLICK ON THE HAMBURGERS ICON') ;
            self.driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]').click();

            self.log.info('CLICK ON LOGOUT LINK') ;
            self.driver.find_element(By.XPATH, '//a[@id="logout_sidebar_link"]').click();

            self.log.info('PRINTING THE STATUS') ;
            print('\n**********TEST CASE IS PASSED********') ;

            self.log.info('TEST CASE IS PASSD') ;
            assert True ;

        except:
            self.log.info('TAKING HE SCREENSHOT') ;
            self.driver.save_screenshot('D:\\PYTEST_JULY\\screenshots\\test_20_02_fail.png') ;

            self.log.info('PRINTING THE STATUS') ;
            print('\n**********TEST CASE IS FAILED********') ;

            self.log.info('TEST CASE IS FAILED') ;
            assert  False ;

        self.log.info('CLOSING THE BROSWER') ;
        self.driver.close() ;

        self.log.info('TEST CASE IS COMPLETED') ;