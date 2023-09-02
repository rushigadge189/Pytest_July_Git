import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_012_dragdrop():
    def test_012(self):
        driver=webdriver.Chrome() ;

        driver.maximize_window();

        driver.get('https://demoqa.com/droppable/') ;

        wait=WebDriverWait(driver,20) ;
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH,'//img[@src="/images/Toolsqa.jpg"]'))) ;

        action=ActionChains(driver) ;

        src=driver.find_element(By.XPATH, '//div[@id="draggable"]') ;
        dest=driver.find_element(By.XPATH, '(//div[@class="drop-box ui-droppable"])[1]') ;

        action.drag_and_drop(src,dest).perform() ;

        driver.save_screenshot("D:\\PYTEST_JULY\\screenshots\\test_012_dd_pass.png") ;

        driver.close();

