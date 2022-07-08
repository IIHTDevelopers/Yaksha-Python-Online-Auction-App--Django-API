from django.contrib import admin
from .models import SellerModel,ProductModel,CustomerModel,BidsModel



class SellerAdmin(admin.ModelAdmin):
    list_display=["seller_id","seller_name","seller_phone_number","seller_email_id","seller_address"]

class ProductAdmin(admin.ModelAdmin):
    list_display=["product_id","seller_id","product_name","product_description","product_price","product_quantity","product_start_bidding_amount","product_last_date_of_bidding","product_category"]

class CustomerAdmin(admin.ModelAdmin):
    list_display=["customer_id","customer_user_name","customer_password","customer_phone_number","customer_email_id","customer_address"]

class BidsAdmin(admin.ModelAdmin):
    list_display=["bid_id","bid_amount","bidding_date","product_id","customer_id"]

admin.site.register(SellerModel,SellerAdmin)
admin.site.register(ProductModel,ProductAdmin)
admin.site.register(CustomerModel,CustomerAdmin)
admin.site.register(BidsModel,BidsAdmin)
