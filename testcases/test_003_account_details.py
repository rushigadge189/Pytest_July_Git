import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_003_pb_details():
    def test_003(self):
        driver=webdriver.Chrome();

        driver.implicitly_wait(5) ;

        driver.maximize_window();

        driver.get('https://para.testar.org/parabank/about.htm;jsessionid=FB240F858FA900BA96DEE5A980656F85');

        driver.find_element(By.XPATH, '//input[@name="username"]').send_keys('rushigadge1897');

        driver.find_element(By.XPATH, '//input[@name="password"]').send_keys('Rushi@181297');

        driver.find_element(By.XPATH, '//input[@value="Log In"]').click();

        try:
            driver.title == 'ParaBank | Accounts Overview' ;
            driver.save_screenshot('D:\\PYTEST_JULY\\screenshots\\details_pass.png') ;
            accno=driver.find_element(By.XPATH, '//a[@class="ng-binding"]').text ;
            print('Account Number= ',accno);
            ammount=driver.find_element(By.XPATH, '(//td[@class="ng-binding"])[1]').text ;
            print('Ammount= ' ,ammount) ;

        except:
            driver.save_screenshot('D:\\PYTEST_JULY\\screenshots\\details_fail.png') ;
            print('Some Error Occured.....!') ;

        driver.close()