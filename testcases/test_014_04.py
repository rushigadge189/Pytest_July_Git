import time
import webbrowser

from Tools.scripts.var_access_benchmark import B
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_py_04():
    def test_div(self):
        g=10;
        h=5;
        div=g/h;
        if(div==2) :
            print('\n DIVISION SUCCESSFUL ') ;
            assert True ;
        else :
            print('\n INVALID OPERTAION') ;
            assert False ;

    def test_0014(self):
        driver=webdriver.Chrome() ;

        driver.implicitly_wait(5) ;

        driver.maximize_window() ;

        driver.get('https://para.testar.org/parabank/index.htm?ConnType=JDBC') ;

        driver.find_element(By.XPATH, '//input[@name="username"]').send_keys('rushigadge1897') ;

        driver.find_element(By.XPATH, '//input[@name="password"]').send_keys('Rushi@181297') ;

        driver.find_element(By.XPATH, '//input[@value="Log In"]').click() ;

        driver.find_element(By.XPATH, '//a[text()="Transfer Funds"]').click() ;

        if( driver.title=='ParaBank | Transfer Funds' ) :

            time.sleep(1) ;
            driver.find_element(By.XPATH, '//input[@id="amount"]').send_keys('100') ;
            time.sleep(2) ;

            driver.find_element(By.XPATH, '//input[@value="Transfer"]').click() ;
            time.sleep(2) ;

            driver.save_screenshot("D:\\PYTEST_JULY\\screenshots\\Test_py_04_pass.png");

            successmsg=driver.find_element(By.XPATH, '(//div[@class="ng-scope"])[1]').text ;
            print(successmsg) ;

            print('\n TEST CASE IS PASSED ') ;

            driver.close();
            assert  True ;
        else:
            driver.save_screenshot("D:\\PYTEST_JULY\\screenshots\\Test_py_04_fail.png");

            print(' \n TEST CASE IS FAILED ') ;

            driver.close() ;
            assert  False;
