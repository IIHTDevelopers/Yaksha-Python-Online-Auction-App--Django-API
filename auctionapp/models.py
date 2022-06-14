from django.db import models
class SellerModel(models.Model):
    seller_id = models.AutoField(primary_key=True)
    seller_name=models.CharField(max_length=100)
    seller_phone_number =models.IntegerField()
    seller_email_id=models.EmailField(max_length=100)
    seller_address=models.CharField(max_length=100)

    def __str__(self):
        return self.seller_name

class ProductModel(models.Model):
    product_id = models.AutoField(primary_key=True)
    #seller_id = models.ForeignKey(SellerModel,on_delete=models.CASCADE,default=0)#
    seller_id = models.IntegerField() # Is it foreign key ??
    product_name=models.CharField(max_length=100)
    product_description=models.CharField(max_length=100)
    product_price =models.DecimalField(max_digits=10,decimal_places=2)
    product_quantity =models.IntegerField()
    product_start_bidding_amount=models.DecimalField(max_digits=10,decimal_places=2)
    product_last_date_of_bidding = models.DateField()
    PRODUCT_CHOICES = (
    ("Mobiles", "Mobiles"),
    ("Electronics", "Electronics"),
    ("Clothing", "Clothing"),
    ("Home", "Home"),
    )
    product_category =models.CharField(max_length=100,choices = PRODUCT_CHOICES,default = 'Mobiles')
    def __str__(self):
        return self.product_name
class CustomerModel(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_user_name=models.CharField(max_length=100)
    customer_password=models.CharField(max_length=100)
    customer_phone_number =models.IntegerField()
    customer_email_id=models.EmailField(max_length=100)
    customer_address=models.CharField(max_length=100)
    def __str__(self):
        return self.customer_user_name
class BidsModel(models.Model):
    bid_id = models.AutoField(primary_key=True)
    bid_amount=models.DecimalField(max_digits=10,decimal_places=2)
    bidding_date = models.DateField(auto_now_add=True) # iS it auto ???
    product_id=models.IntegerField()
    customer_id=models.IntegerField()
    def __str__(self):
        return self.bid_id
