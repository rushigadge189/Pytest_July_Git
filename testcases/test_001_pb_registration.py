import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_001_pb_reg():
    def test_001(self):
        driver=webdriver.Chrome() ;
        time.sleep(1) ;

        driver.maximize_window();
        time.sleep(1);

        driver.get("https://para.testar.org/parabank/about.htm;jsessionid=FB240F858FA900BA96DEE5A980656F85") ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//a[text()="Register"]').click() ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@id="customer.firstName"]').send_keys('Rushikesh') ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@id="customer.lastName"]').send_keys('Gadge') ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@name="customer.address.street"]').send_keys('201/A, Santosh Darshan') ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@id="customer.address.city"]').send_keys('Dombivli') ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@name="customer.address.state"]').send_keys('Maharashtra')
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@name="customer.address.zipCode"]').send_keys('421 201') ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@id="customer.phoneNumber"]').send_keys('1234567890') ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@id="customer.ssn"]').send_keys('CSR12345') ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@id="customer.username"]').send_keys('rushigadge1897');
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@id="customer.password"]').send_keys('Rushi@181297') ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@id="repeatedPassword"]').send_keys('Rushi@181297') ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '(//input[@class="button"])[2]').click();
        time.sleep(5) ;

        if(driver.title == 'ParaBank | Customer Created') :
                driver.save_screenshot("D:\\PYTEST_JULY\\screenshots\\reg_pass.png") ;
                print('Registration Successful') ;
        else:
            driver.save_screenshot("D:\\PYTEST_JULY\\screenshots\\reg_fail.png");
            print('Some Error Occured......!') ;


        driver.close();
