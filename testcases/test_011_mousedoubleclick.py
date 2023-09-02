import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


class Test_011_double_click():
    def test_011(self):

        driver=webdriver.Chrome() ;

        driver.implicitly_wait(5) ;

        driver.maximize_window();

        driver.get('https://demo.guru99.com/test/simple_context_menu.html') ;

        action=ActionChains(driver) ;

        dclick=driver.find_element(By.XPATH, '//button[@ondblclick="myFunction()"]') ;
        action.double_click(dclick).perform() ;

        text1=Alert(driver).text ;
        print('\n**********ALERT TEXT*********\n',text1) ;

        Alert(driver).accept();

        driver.close();
