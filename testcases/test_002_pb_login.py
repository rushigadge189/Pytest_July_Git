import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_002_pb_login() :
    def test_002(self):
        driver=webdriver.Chrome() ;
        time.sleep(1);

        driver.maximize_window();
        time.sleep(1);

        driver.get('https://para.testar.org/parabank/about.htm;jsessionid=FB240F858FA900BA96DEE5A980656F85');
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@name="username"]').send_keys('rushigadge1897');
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@name="password"]').send_keys('Rushi@181297') ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@value="Log In"]').click() ;
        time.sleep(1);

        if (driver.title=='ParaBank | Accounts Overview') :
            driver.save_screenshot("D:\\PYTEST_JULY\\screenshots\\login_pass.png") ;
            print('Login Successful') ;
        else:
            driver.save_screenshot("D:\PYTEST_JULY\screenshots\login_fail.png") ;
            print('Some Error Occured') ;
        
        driver.close();