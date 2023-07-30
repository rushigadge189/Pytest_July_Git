import pytest

class Test_User_Marker() :

    @pytest.mark.customer
    def test_add_cust ( self ) :
        print ( 'Customer Added Successfully') ;

    @pytest.mark.customer
    def test_delete_cust ( self ) :
        print ('Customer Deleted Successfully') ;

    @pytest.mark.customer
    def test_update_cust ( self ) :
        print ( 'Customer Updated Successfully' ) ;

    @pytest.mark.product
    def test_add_prod ( self ) :
        print ( 'Product Added Successfully' ) ;

    @pytest.mark.product
    def test_delete_prod ( self ) :
        print ( 'Product Deleted Successfully' ) ;

    @pytest.mark.product
    def test_update_prod ( self ) :
        print ( 'Product Updated Successfully' ) ;

    @pytest.mark.bill
    def test_bill ( self ) :
        print ( 'Bill Generated Successfully' ) ;
