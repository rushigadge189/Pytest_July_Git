import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_14_fixture():
    def test_017_01(self,setup):
        self.driver=setup ;

        self.driver.get("https://para.testar.org/parabank/about.htm;jsessionid=FB240F858FA900BA96DEE5A980656F85");

        if ( self.driver.title=='ParaBank | About Us' ) :
            print('\nYOU ARE AT THE RIGHT PAGE') ;
            self.driver.save_screenshot("D:\\PYTEST_JULY\\screenshots\\test_017_01_pass.png") ;
            self.driver.close();

            assert True ;
        else:
            print('\nOOPS...! YOU ENTERED WRONG URL') ;
            self.driver.save_screenshot('D:\\PYTEST_JULY\\screenshots\\test_017_01_fail.png') ;
            self.driver.close() ;

            assert False ;
    def test_017_02(self,setup):
        self.driver=setup ;

        self.driver.get("https://para.testar.org/parabank/about.htm;jsessionid=FB240F858FA900BA96DEE5A980656F85");

        self.driver.find_element(By.XPATH, '//input[@name="username"]').send_keys('rushigadge1897')

        self.driver.find_element(By.XPATH, '(//input[@class="input"])[2]').send_keys('Rushi@181297') ;

        self.driver.find_element(By.XPATH, '//input[@value="Log In"]').click() ;

        if( self.driver.title== 'ParaBank | Accounts Overview' ) :
            self.driver.save_screenshot('D:\\PYTEST_JULY\\screenshots\\test_017_02_pass.png') ;
            print('\nLOGIN SUCCESSFUL') ;

            self.driver.find_element(By.XPATH, '//a[text()="Log Out"]').click();
            self.driver.close() ;

            assert True ;
        else:
            self.driver.save_screenshot('D:\\PYTEST_JULY\\screenshots\\test_017_02_fail.png');
            print('\nLOGIN FAILED') ;
            self.driver.close();
            assert False ;

    def test_17_03(self,setup):
        self.driver=setup ;

        self.driver.get("https://para.testar.org/parabank/about.htm;jsessionid=FB240F858FA900BA96DEE5A980656F85");

        self.driver.find_element(By.XPATH, '//input[@name="username"]').send_keys('rushigadge1897')

        self.driver.find_element(By.XPATH, '(//input[@class="input"])[2]').send_keys('Rushi@181297');

        self.driver.find_element(By.XPATH, '//input[@value="Log In"]').click();

        self.driver.find_element(By.XPATH, '//a[text()="Accounts Overview"]').click() ;

        try:
            self.driver.find_element(By.XPATH, '//h1[@class="title"]') ;

            accno=self.driver.find_element(By.XPATH, '//a[@class="ng-binding"]').text ;
            print('\nACCOUNT NUMBER=' ,accno) ;

            accbalance=self.driver.find_element(By.XPATH, '(//td[@class="ng-binding"])[2]').text ;
            print('\nACCPUNT BALANCE=' ,accbalance) ;

            self.driver.save_screenshot('D:\\PYTEST_JULY\\screenshots\\test_017_03_pass.png');
            print('\nACCOUNT DETAILS PRINTED SUCESSFULLY') ;

            self.driver.find_element(By.XPATH, '//a[text()="Log Out"]').click() ;

            self.driver.close();

            assert True ;

        except :
            self.driver.save_screenshot('D:\\PYTEST_JULY\\screenshots\\test_017_03_fail.png');
            print('\nUNABLE TO PRINT THE ACCOUNT DETAILS') ;
            self.driver.close();

            assert False ;




