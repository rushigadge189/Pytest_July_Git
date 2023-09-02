from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_py_01():
    def test_add_001(self):
        a=10 ;
        b=5 ;
        add=a+b ;
        if (add==15) :
            print(' \n ADDITION SUCCESSFUL ') ;
            assert True ;
        else :
            print(' \n INVALID OPERATION ') ;
            assert False ;

    def test_0012(self):

        driver=webdriver.Chrome();

        driver.implicitly_wait(5) ;

        driver.maximize_window();

        driver.get('https://para.testar.org/parabank/index.htm?ConnType=JDBC') ;

        if( driver.title=='ParaBank | Welcome | Online Banking' ) :
            driver.save_screenshot('D:\\PYTEST_JULY\\screenshots\\Test_py_01_pass.png') ;
            print(' \n YOU ARE AT PARASOFT ') ;
            driver.close() ;
            assert True ;

        else :
            driver.save_screenshot('D:\\PYTEST_JULY\\screenshots\\Test_py_01_fail.png')
            print(' \n YOU ARE AT WRONG URL ') ;
            driver.close() ;
            assert False ;


