import pytest


class Test_py_015_markers():
    def test_add(self):
        a=10;
        b=5;
        add=a+b;
        print('ADDITION=',add) ;
        if(add==15) :
            assert True;
        else:
            assert False ;
    @pytest.mark.skip
    def test_sub(self):
        a=10;
        b=5;
        sub=a-b;
        print('SUBSTRACTION=',sub) ;
        if(sub==5) :
            assert True ;
        else:
            assert False ;

    @pytest.mark.xfail
    def test_mul(self):
        a=10 ;
        b=5;
        mul=a*b;
        print('MULTIPLICATION=',mul) ;
        if(mul==50) :
            assert True ;
        else :
            assert False ;

    @pytest.mark.skipif
    def test_div(self):
        a=10;
        b=5;
        div=a/b;
        print('DIVISION=',div) ;
        if(div==2) :
            assert True ;
        else:
            assert  False ;
