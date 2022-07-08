
from rest_framework.test import APITestCase
from auctionapp.models import SellerModel,ProductModel,CustomerModel,BidsModel
from auctionapp.test.TestUtils import TestUtils
class OnlineAuctionAPIExceptionalTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        SellerModel.objects.create(
        seller_name= "Seller1",
        seller_phone_number= 9485843958,
        seller_email_id= "Seller1@gmail.com",
        seller_address= "Vizag")

        ProductModel.objects.create(
        product_id=1,
        seller_id=1,
        product_name= "Samsung",
        product_description="Samsung is a mobile",
        product_price=25000.00,
        product_quantity=1,
        product_start_bidding_amount=30000.00,
        product_last_date_of_bidding='2022-06-05',
        product_category="Mobiles"
        )

        CustomerModel.objects.create(
        customer_id=2,
        customer_user_name= "Customer2",
        customer_password= "venu123",
        customer_phone_number= 9951849555,
        customer_email_id= "customer2@gmail.com",
        customer_address= "Tirupathi")

        BidsModel.objects.create(
        bid_id= 1,
        bid_amount="32000.00",
        bidding_date='2022-06-01',
        product_id= 1,
        customer_id= 2
        )

    def test_post_request_for_seller_with_insuffuficient_details(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/seller/'
        data={
        #"seller_id": 3,
        "seller_name": "Seller2",
        "seller_phone_number": 9885843951,
        "seller_email_id": "Seller2@gmail.com"
        }
        response=self.client.post(url,data,format='json')
        if response.status_code==500:
            test_obj.yakshaAssert("TestPostRequestForSellerWithInsuffuficientDetails", True, "exception")
            print("TestPostRequestForSellerWithInsuffuficientDetails = Passed")
        else:
            test_obj.yakshaAssert("TestPostRequestForSellerWithInsuffuficientDetails", False, "exception")
            print("TestPostRequestForSellerWithInsuffuficientDetails = Failed")

    def test_get_request_for_all_records_of_seller_with_url_mismatch(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/sellers/'
        response=self.client.get(url)
        if response.status_code==404:
            test_obj.yakshaAssert("TestGetRequestForAllRecordsOfSellerWithUrlMismatch", True, "exception")
            print("TestGetRequestForAllRecordsOfSellerWithUrlMismatch = Passed")
        else:
            test_obj.yakshaAssert("TestGetRequestForAllRecordsOfSellerWithUrlMismatch", False, "exception")
            print("TestGetRequestForAllRecordsOfSellerWithUrlMismatch = Failed")

    def test_get_request_for_non_exist_record_of_seller(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/seller_id/222/'
        response=self.client.get(url)
        if response.status_code==500:
            test_obj.yakshaAssert("TestGetRequestForNonExistRecordOfSeller", True, "exception")
            print("TestGetRequestForNonExistRecordOfSeller = Passed")
        else:
            test_obj.yakshaAssert("TestGetRequestForNonExistRecordOfSeller", False, "exception")
            print("TestGetRequestForNonExistRecordOfSeller = Failed")

    def test_delete_request_of_non_exist_seller(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/seller_id/1111/'
        response=self.client.delete(url)
        if response.status_code==500:
            test_obj.yakshaAssert("TestDeleteRequestOfNonExistSeller", True, "exception")
            print("TestDeleteRequestOfNonExistSeller = Passed")
        else:
            test_obj.yakshaAssert("TestDeleteRequestOfNonExistSeller", False, "exception")
            print("TestDeleteRequestOfNonExistSeller = Failed")

    def test_post_request_for_product_with_insuffuficient_details(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/product/'
        data={
        "seller_id": 3,
        "product_name": "Samsung",
        "product_description": "Samsung is a mobile",
        "product_price": "25000.00",
        "product_quantity": 1,
        "product_start_bidding_amount": "30000.00"
        }
        response=self.client.post(url,data,format='json')
        if response.status_code==500:
            test_obj.yakshaAssert("TestPostRequestForProductWithInsuffuficientDetails", True, "exception")
            print("TestPostRequestForProductWithInsuffuficientDetails = Passed")
        else:
            test_obj.yakshaAssert("TestPostRequestForProductWithInsuffuficientDetails", False, "exception")
            print("TestPostRequestForProductWithInsuffuficientDetails = Failed")

    def test_delete_request_of_non_exist_product(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/product_id/1111/'
        response=self.client.delete(url)
        if response.status_code==500:
            test_obj.yakshaAssert("TestDeleteRequestOfNonExistProduct", True, "exception")
            print("TestDeleteRequestOfNonExistProduct = Passed")
        else:
            test_obj.yakshaAssert("TestDeleteRequestOfNonExistProduct", False, "exception")
            print("TestDeleteRequestOfNonExistProduct = Failed")

    def test_get_request_for_non_exist_product_by_seller(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/get_products/?seller_id=111'
        response=self.client.get(url)
        if response.status_code==500:
            test_obj.yakshaAssert("TestGetRequestForNonExistProductsBySeller", True, "exception")
            print("TestGetRequestForNonExistProductsBySeller = Passed")
        else:
            test_obj.yakshaAssert("TestGetRequestForNonExistProductsBySeller", False, "exception")
            print("TestGetRequestForNonExistProductsBySeller = Failed")

    def test_get_request_for_non_exist_bids_by_product(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/list_products/?product_id=111'
        response=self.client.get(url)
        if response.status_code==500:
            test_obj.yakshaAssert("TestGetRequestForNonExistBidsByProduct", True, "exception")
            print("TestGetRequestForNonExistBidsByProduct = Passed")
        else:
            test_obj.yakshaAssert("TestGetRequestForNonExistBidsByProduct", False, "exception")
            print("TestGetRequestForNonExistBidsByProduct = Failed")

#---Customer Functionalities

    def test_get_request_for_non_exist_record_of_product(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/product_id/1111/'
        response=self.client.get(url)
        if response.status_code==500:
            test_obj.yakshaAssert("TestGetRequestForNonExistRecordOfProduct ", True, "exception")
            print("TestGetRequestForNonExistRecordOfProduct  = Passed")
        else:
            test_obj.yakshaAssert("TestGetRequestForNonExistRecordOfProduct ", False, "exception")
            print("TestGetRequestForNonExistRecordOfProduct  = Failed")

    def test_post_request_for_customer_with_insuffuficient_details(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/customer/'
        data=    {
        #"customer_id": 1,
        "customer_user_name": "Customer1",
        "customer_password": "venu123",
        "customer_phone_number": 9951849634,
        "customer_email_id": "customer1@gmail.com"
        }
        response=self.client.post(url,data,format='json')
        if response.status_code==500:
            test_obj.yakshaAssert("TestPostRequestForCustomerWithInsuffuficientDetails", True, "exception")
            print("TestPostRequestForCustomerWithInsuffuficientDetails = Passed")
        else:
            test_obj.yakshaAssert("TestPostRequestForCustomerWithInsuffuficientDetails", False, "exception")
            print("TestPostRequestForCustomerWithInsuffuficientDetails = Failed")

    def test_get_request_for_non_exist_record_of_customer(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/customer_id/222/'
        response=self.client.get(url)
        if response.status_code==500:
            test_obj.yakshaAssert("TestGetRequestForNonExistRecordOfCustomer", True, "exception")
            print("TestGetRequestForNonExistRecordOfCustomer = Passed")
        else:
            test_obj.yakshaAssert("TestGetRequestForNonExistRecordOfCustomer", False, "exception")
            print("TestGetRequestForNonExistRecordOfCustomer = Failed")

    def test_put_request_for_customer_with_insuffuficient_details(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/customer_id/2/'
        data=    {
        "customer_id": 2,
        "customer_user_name": "Customer1",
        "customer_password": "venu123",
        "customer_phone_number": 9951849634
        }
        response=self.client.put(url,data,format='json')
        if response.status_code==500:
            test_obj.yakshaAssert("TestPutRequestForCustomerWithInsuffuficientDetails", True, "exception")
            print("TestPutRequestForCustomerWithInsuffuficientDetails = Passed")
        else:
            test_obj.yakshaAssert("TestPutRequestForCustomerWithInsuffuficientDetails", False, "exception")
            print("TestPutRequestForCustomerWithInsuffuficientDetails = Failed")

    def test_post_request_for_bids_with_no_product_id(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/place_bid/?customer_id=2'
        data=    {
        "bid_id": 1,
        "bid_amount": "32000.00",
        "bidding_date": "2022-06-01",
        "product_id": 1,
        "customer_id": 2
        }
        response=self.client.post(url,data,format='json')
        if response.status_code==500:
            test_obj.yakshaAssert("TestPostRequestForBidsWithNoProductId", True, "exception")
            print("TestPostRequestForBidsWithNoProductId = Passed")
        else:
            test_obj.yakshaAssert("TestPostRequestForBidsWithNoProductId", False, "exception")
            print("TestPostRequestForBidsWithNoProductId = Failed")

    def test_get_request_for_bids_by_non_exist_date(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/list_products_by_date/?product_id=1&bidding_date=2000-06-01'
        response=self.client.get(url)
        if response.status_code==500:
            test_obj.yakshaAssert("TestGetRequestForBidsByNonExistDate", True, "exception")
            print("TestGetRequestForBidsByNonExistDate = Passed")
        else:
            test_obj.yakshaAssert("TestGetRequestForBidsByNonExistDate", False, "exception")
            print("TestGetRequestForBidsByNonExistDate = Failed")

    def test_get_request_for_bids_by_non_exist_category(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/list_products_by_category/?customer_id=1'
        response=self.client.get(url)
        if response.status_code==500:
            test_obj.yakshaAssert("TestGetRequestForBidsByNonExistCategory", True, "exception")
            print("TestGetRequestForBidsByNonExistCategory = Passed")
        else:
            test_obj.yakshaAssert("TestGetRequestForBidsByNonExistCategory", False, "exception")
            print("TestGetRequestForBidsByNonExistCategory = Failed")
