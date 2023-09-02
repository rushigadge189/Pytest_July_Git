from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_py_03() :
    def test_mul(self):
        e=10;
        f=5;
        mul=e*f;
        if(mul==50) :
            print('\n MULTIPLICATION SUCCESSFUL') ;
            assert True ;
        else:
            print(' INVALID OPERATION ') ;
            assert False ;


    def test_0013(self):

        driver = webdriver.Chrome();

        driver.implicitly_wait(5);

        driver.maximize_window();

        driver.get('https://para.testar.org/parabank/index.htm?ConnType=JDBC');

        driver.find_element(By.XPATH, '//input[@name="username"]').send_keys('rushigadge1897');

        driver.find_element(By.XPATH, '//input[@name="password"]').send_keys('Rushi@181297');

        driver.find_element(By.XPATH, '//input[@value="Log In"]').click() ;

        driver.find_element(By.XPATH, '//a[text()="Accounts Overview"]').click() ;

        if (driver.title == 'ParaBank | Accounts Overview'):
            driver.save_screenshot('D:\\PYTEST_JULY\\screenshots\\Test_py_03_pass.png');

            account = driver.find_element(By.XPATH, '//a[@class="ng-binding"]').text;
            print(' \n ACCOUNT NUMBER = ', account);

            ammount = driver.find_element(By.XPATH, '(//td[@class="ng-binding"])[2]').text;
            print(' \n AMMOUNT =', ammount);

            print(' \n DETAILS PRINT SUCCESSFULLY ') ;
            driver.find_element(By.XPATH, '//a[text()="Log Out"]').click();
            driver.close();
            assert True;

        else:
            driver.save_screenshot('D:\\PYTEST_JULY\\screenshots\\test_py_03_fail.png');
            print(' \n UNABLE TO PRINT THE DETAILS ');
            driver.close();
            assert False;