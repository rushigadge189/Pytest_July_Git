import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities import XUTils
class Test_19_03_orange_hrm() :
    def test_19_03_ohrm(self):
        driver=webdriver.Chrome() ;

        driver.maximize_window();

        driver.implicitly_wait(5) ;

        file="D:\\PYTEST_JULY\\testdata\\DDT_Orange_HRM.xlsx" ;

        rows=XUTils.getRowCount(file, 'OHRM')

        for r in range(2, rows+1) :
            driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login') ;

            username=XUTils.readData(file, 'OHRM', r, 1) ;
            password=XUTils.readData(file, 'OHRM', r ,2) ;

            driver.find_element(By.XPATH, '//input[@name="username"]').send_keys(username) ;

            driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(password) ;

            driver.find_element(By.XPATH, '//button[@type="submit"]').click() ;

            try:
                driver.find_element(By.XPATH, '//h6[@class="oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module"]') ;

                XUTils.writeData(file, 'OHRM', r, 3, 'Passed');
                print('\nTEST CASE IS PASSED.........!') ;

                driver.find_element(By.XPATH, '//p[@class="oxd-userdropdown-name"]').click() ;
                time.sleep(1) ;

                driver.find_element(By.XPATH, '//a[text()="Logout"]').click() ;
                time.sleep(1) ;

            except:
                XUTils.writeData(file, 'OHRM', r, 3, 'FAILED') ;
                print('\nTEST CASE IS FAILED.........!');

        driver.close();


