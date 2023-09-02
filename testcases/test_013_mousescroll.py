import time

from selenium import webdriver


class Test_013_mouse_sroll():
    def test_013(self):
        driver=webdriver.Chrome();

        driver.maximize_window();

        time.sleep(1) ;

        driver.get('https://www.lambdatest.com/blog/scroll-a-webpage-in-selenium-using-java/') ;

        driver.save_screenshot("D:\\PYTEST_JULY\\screenshots\\test_013_beforescroll.png")

        driver.execute_script("window.scrollBy(0,1000)") ;

        driver.save_screenshot("D:\\PYTEST_JULY\\screenshots\\test_013_afterscroll.png") ;

        driver.close();