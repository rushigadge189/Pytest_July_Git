import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_006_implicit_wait():

    def test_006_iwait(self):
        driver=webdriver.Chrome() ;

        driver.implicitly_wait(30) ;

        driver.maximize_window();

        driver.get('https://www.google.co.in/') ;

        driver.find_element(By.XPATH, '//textarea[@class="gLFyf"]').send_keys('Test Internet Speed') ;

        allsugg=driver.find_elements(By.XPATH, '//*[@id="Alh6id"]/div[1]/div/ul/li[3]/../li');
        length1=len(allsugg)
        print("\n Total Autosuggestion= " ,length1) ;

        for results in allsugg:
            print('\n Suggestion=',results.text) ;

        driver.find_element(By.XPATH, '(//input[@class="gNO89b"])[1]').click() ;

        driver.find_element(By.XPATH, '//div[text()="RUN SPEED TEST"]').click();
        time.sleep(30) ;

        upload=driver.find_element(By.XPATH, '//p[@jsname="Lk0VKd"]').text ;
        print('\n UPLOAD SPEED=' ,upload +'MBPS') ;

        download=driver.find_element(By.XPATH, '//p[@jsname="dSdcdd"]').text ;
        print('\n DOWNLOAD SPEED=' ,download +'MBPS') ;

        driver.save_screenshot('D:\\PYTEST_JULY\\screenshots\\test_006_internet_pass.png');
        driver.close();
