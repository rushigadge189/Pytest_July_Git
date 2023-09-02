import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


class Test_004_alerts_test():
    def test_004_alert(self):

        driver = webdriver.Chrome();

        driver.implicitly_wait(5);

        driver.delete_all_cookies();

        driver.maximize_window();

        driver.get('https://chercher.tech/practice/practice-pop-ups-selenium-webdriver');

        driver.find_element(By.XPATH, '//input[@value="Alert"]').click() ;
        time.sleep(1) ;

        msg1=Alert(driver).text ;
        print("\nAlert1 Message = ",msg1) ;

        Alert(driver).accept() ;

        driver.close() ;

    def test_04_confirm_alert(self):

        driver = webdriver.Chrome();

        driver.implicitly_wait(5);

        driver.delete_all_cookies();

        driver.maximize_window();

        driver.get('https://chercher.tech/practice/practice-pop-ups-selenium-webdriver');

        driver.find_element(By.XPATH, '//input[@value="Confirmation Box"]').click();
        time.sleep(1) ;

        msg2=Alert(driver).text ;
        print('\nConfirmantion Alert Maeeage = ',msg2) ;

        Alert(driver).accept() ;
        #Alert(driver).dismiss() ;

        driver.close() ;

    def test_004_prompt_alert(self):

        driver=webdriver.Chrome() ;

        driver.maximize_window() ;

        driver.implicitly_wait(5) ;

        driver.delete_all_cookies() ;

        driver.get('https://the-internet.herokuapp.com/javascript_alerts') ;

        driver.find_element(By.XPATH, '//button[@onclick="jsPrompt()"]').click();
        time.sleep(1);

        msg3=Alert(driver).text;
        print('Prompt Alert Message =',msg3) ;
        time.sleep(1) ;

        Alert(driver).send_keys('My, Name Is Anthony Gonsalves');

        Alert(driver).accept();

        Prompt = driver.find_element(By.XPATH, '//p[@id="result"]').text;
        print(Prompt);
        time.sleep(1);

        driver.close();






