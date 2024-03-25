import time

from selenium import webdriver


class Test_Credence_001 () :
    def test_sum_001 (self):
        a = 3 ;
        b = 7 ;
        sum = a + b ;
        print ( 'Sum Of A And B = ', sum ) ;
        if ( sum == 10) :
            assert True ;
        else :
            assert False ;


    def test_CredenceURL_002 ( self ) :
        driver = webdriver.Chrome() ;
        time.sleep(1) ;

        driver.maximize_window();
        time.sleep(1) ;

        driver.get('https://www.credence.in/') ;
        time.sleep(1) ;

        if ( driver.title == 'Credence' ) :
            print ( 'You Are At Credence. in' ) ;
            driver.close() ;
            assert True;
        else :
            print ( 'You Are Entered The Wrong URL' ) ;
            driver.close() ;
            assert False;

    def test_sub_003 ( self ) :
        a = 3 ;
        b = 7 ;
        sub = a - b ;
        print ( 'substraction Od A And B =' ,sub ) ;
        if ( sub == -4 ) :
            assert True ;
        else:
            assert False ;

