import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities import XUTils ;

class Test_19_parabank_ddt():
    def test_parabank(self):
        driver=webdriver.Chrome() ;

        driver.maximize_window();

        driver.implicitly_wait(5) ;

        path="D:\\PYTEST_JULY\\testdata\\DDT_Parabank.xlsx" ;

        rows=XUTils.getRowCount(path,'PARABANK') ;

        for r in range(2, rows+1) :

            driver.get('https://para.testar.org/parabank/about.htm;jsessionid=FB240F858FA900BA96DEE5A980656F85');

            username=XUTils.readData(path,'PARABANK', r, 1 );
            password=XUTils.readData(path,'PARABANK',r, 2) ;

            driver.find_element(By.XPATH,'//input[@name="username"]').send_keys(username) ;

            driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(password) ;

            driver.find_element(By.XPATH, '//input[@value="Log In"]').click() ;

            if (driver.title=='ParaBank | Accounts Overview') :
                print('\nTEST CASE IS PASSED.........!') ;
                XUTils.writeData(path,'PARABANK',r, 3, 'PASSED') ;

                driver.find_element(By.XPATH,'//a[text()="Log Out"]').click() ;

            else:
                print('\nTEST CASE IS FAILED.......!') ;
                XUTils.writeData(path,'PARABANK', r, 3, 'FAILED') ;

        driver.close();




