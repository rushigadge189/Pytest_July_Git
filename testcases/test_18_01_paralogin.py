import time

from selenium import webdriver
from pageobjects.test_18_01_parabank_login_pages import Test_18_login_pages

class Test_18_pblogin():
    def test_18(self):
        driver=webdriver.Chrome();

        driver.maximize_window();

        driver.implicitly_wait(5) ;

        lpobj=Test_18_login_pages(driver) ;

        lpobj.test_enter_url('https://para.testar.org/parabank/about.htm;jsessionid=FB240F858FA900BA96DEE5A980656F85') ;

        lpobj.test_enter_username('rushigadge1897') ;

        lpobj.test_enter_password('Rushi@181297') ;

        lpobj.test_click_login() ;

        if (lpobj.test_login_status() == True):
            driver.save_screenshot('D:\\PYTEST_JULY\\screenshots\\test_18_01_pass.png');
            print('\nLOGIN SUCCESSFUL.......!');
        else:
            driver.save_screenshot('D:\\PYTEST_JULY\\screenshots\\test_18_01_fail.png');
            print('\nLOGIN UNSUCCESSFUL........!');

        lpobj.test_click_logout() ;
        time.sleep(1);

        driver.close();
