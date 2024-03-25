import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities import XUTils
class Test_19_02_ddtswaglabs():

    def test_19_02_swaglabs(self):

        driver=webdriver.Chrome() ;

        driver.maximize_window();

        driver.implicitly_wait(5);

        path="D:\\PYTEST_JULY\\testdata\\DDT_Swag_Labs.xlsx" ;

        rows=XUTils.getRowCount(path, 'SWAGLABS')

        for r in range(2, rows+1) :

            driver.get('https://www.saucedemo.com/');

            username=XUTils.readData(path, 'SWAGLABS', r, 1) ;
            password=XUTils.readData(path, 'SWAGLABS', r, 2);

            driver.find_element(By.XPATH, '//input[@id="user-name"]').send_keys(username);

            driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(password) ;

            driver.find_element(By.XPATH, '//input[@type="submit"]').click() ;

            try:
                driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]') ;

                XUTils.writeData(path, 'SWAGLABS', r, 3, 'PASSED') ;
                print('\nTEST CASE IS PASSED.......!') ;

                driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]').click();

                driver.find_element(By.XPATH, '//a[@id="logout_sidebar_link"]').click();

            except:
                XUTils.writeData(path, 'SWAGLABS', r, 3,'FAILED') ;
                print('\nTEST CASE IS FAILED.......!') ;

        driver.close();






