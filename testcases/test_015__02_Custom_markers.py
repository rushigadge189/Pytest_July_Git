import pytest


class Test_py_user_markers() :
    @pytest.mark.customer
    def test_add_cust(self):
        print('Customer Added successfully') ;

    @pytest.mark.customer
    def test_del_cust(self):
        print('Customer Deleted Successfully') ;

    @pytest.mark.customer
    def test_search_cust(self):
        print('Customer Searched Successfully') ;

    @pytest.mark.customer
    def test_update_cust(self):
        print('Customer Updated Successsfully') ;



    @pytest.mark.product
    def test_add_prod(self):
        print('Product Added Successfully') ;

    @pytest.mark.product
    def test_del_prod(self):
        print('Product Deleted Sucessfully') ;

    @pytest.mark.product
    def test_search_prod(self):
        print('Product Searched Successfully') ;

    @pytest.mark.product
    def test_update_prod(self):
        print('Product Updated successfully') ;



    @pytest.mark.bill
    @pytest.mark.sanity
    def test_add_bil(self):
        print('Bill Added Successfully') ;

    @pytest.mark.bill
    def test_del_bill(self):
        print('Bill Deleted Successfully') ;

    @pytest.mark.bill
    def test_search_bill(self):
        print('Bill Searched Successfully') ;

    @pytest.mark.bill
    def test_update_bill(self):
        print('Bill Updated Successfully') ;