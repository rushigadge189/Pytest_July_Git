import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_007_explicit_wait() :

    def test_007(self):

        driver=webdriver.Chrome() ;

        driver.implicitly_wait(5) ;

        driver.maximize_window() ;

        driver.get('https://www.google.co.in') ;

        driver.find_element(By.XPATH, '//textarea[@jsname="yZiJbe"]').send_keys('Internet Speed Test') ;

        driver.find_element(By.XPATH, '(//input[@aria-label="Google Search"])[1]').click() ;

        driver.find_element(By.XPATH, '//div[text()="RUN SPEED TEST"]').click() ;

        try:
            wait=WebDriverWait(driver,25,poll_frequency=0.5) ;
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//div[text()="TEST AGAIN"]'))) ;

            downspeed=driver.find_element(By.XPATH, '//div[@class="oyUhj"]').text ;
            print('\n**********DOWNLOAD SPEED********\n',downspeed) ;

            upspeed=driver.find_element(By.XPATH,'//div[@class="iD3Ij"]').text ;
            print('\n**********UPLOAD SPEED**********\n',upspeed) ;
            time.sleep(1) ;

            driver.save_screenshot("D:\\PYTEST_JULY\\screenshots\\test_007_pass.png");
            assert True ;

        except:
            print('Some Error Occured......!') ;
            driver.save_screenshot("D:\\PYTEST_JULY\\screenshots\\test007_fail.png")
            assert False;

        driver.close() ;