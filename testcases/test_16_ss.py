from selenium import webdriver


class Test_015_screenshot():
    def test_015_sreenshot(self):
        driver=webdriver.Chrome() ;

        driver.implicitly_wait(5);

        driver.maximize_window();

        driver.get('https://para.testar.org/parabank/about.htm;jsessionid=FB240F858FA900BA96DEE5A980656F85');

        if( driver.title=='ParaBank | About Us' ) :

            driver.save_screenshot("D:\\PYTEST_JULY\\screenshots\\test_015_ss_pass.png") ;
            print('\nYOU ARE AT THE RIGHT PAGE') ;
            driver.close();
            assert True ;

        else:
            driver.save_screenshot("D:\\PYTEST_JULY\\screenshots\\test_015_ss_fail.png") ;
            print('\nYOU ARE AT THE WRONG PLACE') ;
            driver.close() ;
            assert False;
    def test_015_sum(self):
        a=10;
        b=20;
        sum=a+b;
        print('\nADDITION=',sum) ;
        if( sum==30 ) :
            print('\nTEST IS PASSED') ;
            assert True;
        else:
            print('\nTEST CASE IS FAILED') ;
            assert False ;