import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


class Test_010_mouse_right_click():
    def test_010(self):
        driver=webdriver.Chrome();

        driver.implicitly_wait(5) ;

        driver.maximize_window();

        driver.get('https://demo.guru99.com/test/simple_context_menu.html') ;

        action=ActionChains(driver) ;

        right_click=driver.find_element(By.XPATH, '//span[@class="context-menu-one btn btn-neutral"]') ;

        action.context_click(right_click).perform() ;

        driver.save_screenshot("D:\\PYTEST_JULY\\screenshots\\test_010_rightclick_pass.png") ;

        driver.find_element(By.XPATH, '//span[text()="Edit"]').click();

        text1=Alert(driver).text ;
        print('\n*********Alert text***********\n', text1) ;

        Alert(driver).accept();

        driver.close() ;


