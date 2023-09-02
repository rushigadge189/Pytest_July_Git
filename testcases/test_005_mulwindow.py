import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_005_multiple_windows() :

    def test_006(self):

        driver=webdriver.Chrome() ;
        time.sleep(1) ;

        driver.maximize_window();
        time.sleep(1);

        driver.get('https://the-internet.herokuapp.com/windows') ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//a[text()="Click Here"]').click();
        time.sleep(2) ;

        allwindow=driver.window_handles ;

        driver.switch_to.window(allwindow[1]) ;
        time.sleep(2) ;

        text1=driver.find_element(By.XPATH, '//h3[text()="New Window"]').text ;
        print('\nText1=', text1) ;
        time.sleep(2) ;

        driver.switch_to.window(allwindow[0]) ;
        time.sleep(1) ;

        text2=driver.find_element(By.XPATH, '//h3[text()="Opening a new window"]').text ;
        print('\nText2=', text2) ;

        driver.close() ;
