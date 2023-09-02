from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_py_02():
    def test_sub(self):
        c=10 ;
        d=5 ;
        sub=c-d ;
        if(sub==5) :
            print(' \n SUBSTRACTION SUCCESSFUL ') ;
            assert True ;
        else :
            print(' \n INVALID OPERATION ') ;
            assert False ;

    def test_0022(self):

        driver = webdriver.Chrome();

        driver.implicitly_wait(5);

        driver.maximize_window();

        driver.get('https://para.testar.org/parabank/index.htm?ConnType=JDBC');

        driver.find_element(By.XPATH, '//input[@name="username"]').send_keys('rushigadge1897');

        driver.find_element(By.XPATH, '//input[@name="password"]').send_keys('Rushi@181297');

        driver.find_element(By.XPATH, '//input[@value="Log In"]').click() ;

        if( driver.title=='ParaBank | Accounts Overview' ) :
            driver.save_screenshot('D:\\PYTEST_JULY\\screenshots\\test_py_02_pass.png') ;
            print(' \n LOGIN SUCCESSFULLY ') ;
            driver.find_element(By.XPATH, '//a[text()="Log Out"]').click() ;
            driver.close() ;
            assert True ;
        else:
            driver.save_screenshot('D:\\PYTEST_JULY\\screenshots\\test_py_02_fail.png');
            print(' \n LOGIN UNSUCCESSFUL ') ;
            driver.close() ;
            assert False ;