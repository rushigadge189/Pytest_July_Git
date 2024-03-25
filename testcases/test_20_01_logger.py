import logging
import time

from selenium import webdriver
from pageobjects.test_18_01_parabank_login_pages import Test_18_login_pages
from utilities.logger import LogGenerator
class Test_20_logger():
    log=LogGenerator.loggen() ;
    def test_20_url(self,setup):
        self.driver=setup
        #********log level EXAMPLE*********#
        print('******************') ;
        self.log.debug('THIS IS THE DEBUG') ;
        self.log.info('THIS IS THE INFO') ;
        self.log.warning('THIS IS WARNING') ;
        self.log.error('THIS IS ERROR');
        self.log.critical('THIS IS CRITICAL');
        print('******************') ;

        self.log.info('TEST CASE FOR URL IS STARTED') ;

        self.obj=Test_18_login_pages(self.driver) ;

        self.log.info('OPENING TEH BROWSER') ;
        self.log.info('ENETRING THE URL') ;

        self.obj.test_enter_url('https://para.testar.org/parabank/about.htm;jsessionid=FB240F858FA900BA96DEE5A980656F85') ;

        self.log.info('CHECKING PAGE TITLE'+self.driver.title) ;

        if(self.driver.title=='ParaBank | About Us') :

            self.log.info('TAKING THE SCREENSHOT') ;

            self.driver.save_screenshot("D:\\PYTEST_JULY\\screenshots\\test_20_url_pass.png") ;

            print('\n**********URL TESTING SUCCESSFUL**********') ;

            self.driver.close() ;

            self.log.info('TEST CASE FOR URL TESTING IS PASSED');
            assert True ;
        else:
            self.log.info('TAKING SCREENSHOT') ;

            self.driver.save_screenshot("D:\\PYTEST_JULY\\screenshots\\test_20_url_fail.png");
            print('\n**********URL TESTING UNSUCCESSFUL**********');
            self.driver.close();

            self.log.info('TEST CASE FOR URL IS FAILED') ;

            assert False ;

        self.log.info('TEST CASE FOR URL IS COMPLETED');
    def test_20_login(self,setup):
        self.driver=setup;

        self.log.info('TEST CASE FOR LOGIN IS STARTED');

        self.log.info('OPENING TEH BROWSER') ;

        self.obj2=Test_18_login_pages(self.driver) ;

        self.log.info('ENTERING THE URL') ;

        self.obj2.test_enter_url('https://para.testar.org/parabank/about.htm;jsessionid=FB240F858FA900BA96DEE5A980656F85') ;

        self.log.info('ENTERING THE USERNAME') ;

        self.obj2.test_enter_username('rushigadge1897') ;

        self.log.info('ENTERING THE PASSWORD') ;

        self.obj2.test_enter_password('Rushi@181297') ;

        self.log.info('CLICK ON LOGIN BUTTON')

        self.obj2.test_click_login() ;

        self.log.info('CHECKING THE STATUS') ;

        if (self.obj2.test_login_status()==True) :
            self.log.info('TAKING THE SCREENSHOT ') ;

            self.driver.save_screenshot('D:\\PYTEST_JULY\\screenshots\\test_20_login_pas.png') ;
            print('**********LOGIN SUCCESSFUL**********') ;

            self.log.info('LOGOUT FROM THE APPLICATION')
            self.obj2.test_click_logout() ;

            self.log.info('CLOSING THE BROWSER');
            self.driver.close() ;

            self.log.info('TEST CASE FOR LOGIN IS PASSED') ;
            assert True ;

        else:
            self.log.info('TAKING SCREENSHOT') ;
            self.driver.save_screenshot('D:\\PYTEST_JULY\\screenshots\\test_20_login_pas.png');
            print('**********LOGIN UNSCCESSFUL**********');

            self.log.info('CLOSING THE BROWSER') ;
            self.driver.close() ;

            self.log.info('TEST CASE FOR LOGIN IS FAILED') ;
            assert False ;


        self.log.info('TEST CASE IS COMPLETED') ;