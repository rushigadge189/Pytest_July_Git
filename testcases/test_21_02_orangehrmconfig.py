import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.ReadConfig import Readconfig

class Test_21_02_orange_hrm():

    username1=Readconfig.getUserName();
    password1=Readconfig.getPassWord() ;
    def test_21_02_ohrm(self):
        driver=webdriver.Chrome() ;

        driver.maximize_window() ;

        driver.implicitly_wait(5) ;

        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login') ;

        driver.find_element(By.XPATH, '//input[@name="username"]').send_keys(self.username1);

        driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(self.password1);

        driver.find_element(By.XPATH, '//button[@type="submit"]').click() ;

        try:

            driver.find_element(By.XPATH, '//img[@alt="profile picture"]');

            driver.save_screenshot("D:\\PYTEST_JULY\\screenshots\\test_21_02_pass.png") ;

            driver.find_element(By.XPATH, '//i[@class="oxd-icon bi-caret-down-fill oxd-userdropdown-icon"]').click() ;

            driver.find_element(By.XPATH, '//a[contains(text(),"Logout")]').click() ;

            print('\n*********LOGIN SUCCESSFUL********');
            driver.close();
            assert True;

        except:
            driver.save_screenshot("D:\PYTEST_JULY\screenshots\\test_21_02_fail.png");
            print('\n*********LOGIN UNSUCCESSFUL********') ;
            driver.close();
            assert False ;