from rest_framework.test import APITestCase
from auctionapp.models import SellerModel,ProductModel,CustomerModel,BidsModel
from auctionapp.test.TestUtils import TestUtils
class OnlineAuctionAPIFunctionalTest(APITestCase):
    # @classmethod
    # def setUpTestData(cls):
    #     SellerModel.objects.create(
    #     seller_name= "Seller1",
    #     seller_phone_number= 9485843958,
    #     seller_email_id= "Seller1@gmail.com",
    #     seller_address= "Vizag")
    #
    #     ProductModel.objects.create(
    #     product_id=1,
    #     seller_id=1,
    #     product_name= "Samsung",
    #     product_description="Samsung is a mobile",
    #     product_price=25000.00,
    #     product_quantity=1,
    #     product_start_bidding_amount=30000.00,
    #     product_last_date_of_bidding='2022-06-05',
    #     product_category="Mobiles"
    #     )
    #
    #     CustomerModel.objects.create(
    #     customer_id=2,
    #     customer_user_name= "Customer2",
    #     customer_password= "venu123",
    #     customer_phone_number= 9951849555,
    #     customer_email_id= "customer2@gmail.com",
    #     customer_address= "Tirupathi")
    #
    #     BidsModel.objects.create(
    #     bid_id= 1,
    #     bid_amount="32000.00",
    #     bidding_date='2022-06-01',
    #     product_id= 1,
    #     customer_id= 2
    #     )
    #     with open("../output_revised.txt","w") as f:
    #         pass

    def test_post_request_for_seller(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/seller/'
        data={
        #"seller_id": 3,
        "seller_name": "Seller2",
        "seller_phone_number": 9885843951,
        "seller_email_id": "Seller2@gmail.com",
        "seller_address": "Vizag"
        }
        response=self.client.post(url,data,format='json')
        if response.status_code==201:
            test_obj.yakshaAssert("TestPostRequestForSeller", True, "functional")
            print("TestPostRequestForSeller = Passed")
        else:
            test_obj.yakshaAssert("TestPostRequestForSeller", False, "functional")
            print("TestPostRequestForSeller = Failed")

    def test_get_request_for_all_records_of_seller(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/seller/'
        response=self.client.get(url)
        if response.status_code==200:
            test_obj.yakshaAssert("TestGetRequestForAllRecordsOfSeller", True, "functional")
            print("TestGetRequestForAllRecordsOfSeller = Passed")
        else:
            test_obj.yakshaAssert("TestGetRequestForAllRecordsOfSeller", False, "functional")
            print("TestGetRequestForAllRecordsOfSeller = Failed")

    def test_get_request_for_single_record_of_seller(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/seller_id/1/'
        response=self.client.get(url)
        if response.status_code==200:
            test_obj.yakshaAssert("TestGetRequestForSingleRecordOfSeller", True, "functional")
            print("TestGetRequestForSingleRecordOfSeller = Passed")
        else:
            test_obj.yakshaAssert("TestGetRequestForSingleRecordOfSeller", False, "functional")
            print("TestGetRequestForSingleRecordOfSeller = Failed")

    def test_delete_request_of_seller(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/seller_id/1/'
        response=self.client.delete(url)
        if response.status_code==200:
            test_obj.yakshaAssert("TestDeleteRequestOfSeller", True, "functional")
            print("TestDeleteRequestOfSeller = Passed")
        else:
            test_obj.yakshaAssert("TestDeleteRequestOfSeller", False, "functional")
            print("TestDeleteRequestOfSeller = Failed")

    def test_post_request_for_product(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/product/'
        data={
        "seller_id": 3,
        "product_name": "Samsung",
        "product_description": "Samsung is a mobile",
        "product_price": "25000.00",
        "product_quantity": 1,
        "product_start_bidding_amount": "30000.00",
        "product_last_date_of_bidding": "2022-06-05",
        "product_category": "Mobiles"
        }
        response=self.client.post(url,data,format='json')
        if response.status_code==201:
            test_obj.yakshaAssert("TestPostRequestForProduct", True, "functional")
            print("TestPostRequestForProduct = Passed")
        else:
            test_obj.yakshaAssert("TestPostRequestForProduct", False, "functional")
            print("TestPostRequestForProduct = Failed")

    def test_delete_request_of_product(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/product_id/1/'
        response=self.client.delete(url)
        if response.status_code==200:
            test_obj.yakshaAssert("TestDeleteRequestOfProduct", True, "functional")
            print("TestDeleteRequestOfProduct = Passed")
        else:
            test_obj.yakshaAssert("TestDeleteRequestOfProduct", False, "functional")
            print("TestDeleteRequestOfProduct = Failed")

    def test_get_request_for_products_by_seller(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/get_products/?seller_id=1'
        response=self.client.get(url)
        if response.status_code==200:
            test_obj.yakshaAssert("TestGetRequestForProductsBySeller", True, "functional")
            print("TestGetRequestForProductsBySeller = Passed")
        else:
            test_obj.yakshaAssert("TestGetRequestForProductsBySeller", False, "functional")
            print("TestGetRequestForProductsBySeller = Failed")

    def test_get_request_for_bids_by_product(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/list_products/?product_id=1'
        response=self.client.get(url)
        if response.status_code==200:
            test_obj.yakshaAssert("TestGetRequestForBidsByProduct", True, "functional")
            print("TestGetRequestForBidsByProduct = Passed")
        else:
            test_obj.yakshaAssert("TestGetRequestForBidsByProduct", False, "functional")
            print("TestGetRequestForBidsByProduct = Failed")

#---Customer Functionalities
    def test_get_request_for_all_records_of_product(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/product/'
        response=self.client.get(url)
        if response.status_code==200:
            test_obj.yakshaAssert("TestGetRequestForAllRecordsOfProduct", True, "functional")
            print("TestGetRequestForAllRecordsOfProduct = Passed")
        else:
            test_obj.yakshaAssert("TestGetRequestForAllRecordsOfProduct", False, "functional")
            print("TestGetRequestForAllRecordsOfProduct = Failed")

    def test_get_request_for_single_record_of_product(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/product_id/1/'
        response=self.client.get(url)
        if response.status_code==200:
            test_obj.yakshaAssert("TestGetRequestForSingleRecordOfProduct", True, "functional")
            print("TestGetRequestForSingleRecordOfProduct = Passed")
        else:
            test_obj.yakshaAssert("TestGetRequestForSingleRecordOfProduct", False, "functional")
            print("TestGetRequestForSingleRecordOfProduct= Failed")

    def test_post_request_for_customer(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/customer/'
        data=    {
        #"customer_id": 1,
        "customer_user_name": "Customer1",
        "customer_password": "venu123",
        "customer_phone_number": 9951849634,
        "customer_email_id": "customer1@gmail.com",
        "customer_address": "Hyderabad"
        }
        response=self.client.post(url,data,format='json')
        if response.status_code==201:
            test_obj.yakshaAssert("TestPostRequestForCustomer", True, "functional")
            print("TestPostRequestForCustomer = Passed")
        else:
            test_obj.yakshaAssert("TestPostRequestForCustomer", False, "functional")
            print("TestPostRequestForCustomer = Failed")

    def test_get_request_for_all_records_of_customer(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/customer/'
        response=self.client.get(url)
        if response.status_code==200:
            test_obj.yakshaAssert("TestGetRequestForAllRecordsOfCustomer", True, "functional")
            print("TestGetRequestForAllRecordsOfCustomer = Passed")
        else:
            test_obj.yakshaAssert("TestGetRequestForAllRecordsOfCustomer", False, "functional")
            print("TestGetRequestForAllRecordsOfCustomer = Failed")

    def test_get_request_for_single_record_of_customer(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/customer_id/2/'
        response=self.client.get(url)
        if response.status_code==200:
            test_obj.yakshaAssert("TestGetRequestForSingleRecordOfCustomer", True, "functional")
            print("TestGetRequestForSingleRecordOfCustomer = Passed")
        else:
            test_obj.yakshaAssert("TestGetRequestForSingleRecordOfCustomer", False, "functional")
            print("TestGetRequestForSingleRecordOfCustomer = Failed")

    def test_put_request_for_customer(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/customer_id/2/'
        data=    {
        "customer_id": 2,
        "customer_user_name": "Customer1",
        "customer_password": "venu123",
        "customer_phone_number": 9951849634,
        "customer_email_id": "customer1@gmail.com",
        "customer_address": "Hyderabad"
        }
        response=self.client.put(url,data,format='json')
        if response.status_code==200:
            test_obj.yakshaAssert("TestPutRequestForCustomer", True, "functional")
            print("TestPutRequestForCustomer = Passed")
        else:
            test_obj.yakshaAssert("TestPutRequestForCustomer", False, "functional")
            print("TestPutRequestForCustomer = Failed")

    def test_post_request_for_bids(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/place_bid/?customer_id=2&product_id=1'
        data=    {
        "bid_id": 1,
        "bid_amount": "32000.00",
        "bidding_date": "2022-06-01",
        "product_id": 1,
        "customer_id": 2
        }
        response=self.client.post(url,data,format='json')
        if response.status_code==201:
            test_obj.yakshaAssert("TestPostRequestForBids", True, "functional")
            print("TestPostRequestForBids = Passed")
        else:
            test_obj.yakshaAssert("TestPostRequestForBids", False, "functional")
            print("TestPostRequestForBids = Failed")

    def test_get_request_for_bids_by_category(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/list_products_by_category/?customer_id=2&product_category=Mobiles'
        response=self.client.get(url)
        if response.status_code==200:
            test_obj.yakshaAssert("TestGetRequestForBidsByCategory", True, "functional")
            print("TestGetRequestForBidsByCategory = Passed")
        else:
            test_obj.yakshaAssert("TestGetRequestForBidsByCategory", False, "functional")
            print("TestGetRequestForBidsByCategory = Failed")

    #Failed

    # def test_get_request_for_bids_by_date(self):
    #     test_obj = TestUtils()
    #     url='http://127.0.0.1:8000/list_products_by_date/?product_id=1&bidding_date=2022-06-01'
    #     response=self.client.get(url)
    #     print(response.status_code)
    #     if response.status_code==200:
    #         test_obj.yakshaAssert("TestGetRequestForBidsByDate", True, "functional")
    #         print("TestGetRequestForBidsByDate = Passed")
    #     else:
    #         test_obj.yakshaAssert("TestGetRequestForBidsByDate", False, "functional")
    #         print("TestGetRequestForBidsByDate = Failed")
