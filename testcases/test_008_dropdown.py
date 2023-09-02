import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Test_008_dropdown() :
    def test_008(self):
        driver=webdriver.Chrome() ;

        driver.implicitly_wait(5) ;

        driver.maximize_window();

        driver.get('https://www.careinsurance.com/rhicl/proposalcp/renew/index-care') ;

        driver.find_element(By.XPATH, '//input[@id="policynumber"]').send_keys('12345') ;

        driver.find_element(By.XPATH, '//input[@placeholder="DOB"]').click() ;

        month=Select(driver.find_element(By.XPATH,'//select[@class="ui-datepicker-month"]')) ;
        month.select_by_visible_text('Dec') ;

        year=Select(driver.find_element(By.XPATH, '//select[@class="ui-datepicker-year"]')) ;
        year.select_by_value('1997');

        driver.find_element(By.XPATH, '//a[text()="18"]').click();

        driver.find_element(By.XPATH, '//input[@placeholder="Contact Number"]').send_keys('1234567890');

        driver.save_screenshot('D:\\PYTEST_JULY\\screenshots\\test_008_dd_pass.png') ;

        driver.close();
