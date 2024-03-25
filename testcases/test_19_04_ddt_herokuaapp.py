import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities import XUTils
class Test_19_04_heroku():

    def test_19_04_heroku_app(self,setup):

        self.driver=setup;

        path="D:\\PYTEST_JULY\\testdata\\DDT_Hiroku.xlsx"
        rows=XUTils.getRowCount(path, 'HEROKU') ;

        for r in range (2, rows+1) :

            self.driver.get('https://the-internet.herokuapp.com/login');
            time.sleep(1);

            username=XUTils.readData(path, 'HEROKU', r, 1) ;
            password=XUTils.readData(path, 'HEROKU', r, 2);

            self.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(username) ;
            time.sleep(1) ;

            self.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(password) ;
            time.sleep(1) ;

            self.driver.find_element(By.XPATH, '//i[contains(text()," Login")]').click() ;
            time.sleep(1) ;

            try:
                self.driver.find_element(By.XPATH, '//i[text()=" Logout"]')

                XUTils.writeData(path, 'HEROKU', r, 3, 'PASSED') ;

                print('\nTEST CASE IS PASSED');

                self.driver.find_element(By.XPATH, '//i[text()=" Logout"]').click();
                time.sleep(1);

            except:
                XUTils.writeData(path, 'HEROKU', r, 3, 'FAILED') ;
                print('\nTEST CASE IS FAILED');

        self.driver.close();



