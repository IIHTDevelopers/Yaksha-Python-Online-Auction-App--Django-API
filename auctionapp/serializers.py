from rest_framework.serializers import ModelSerializer
from .models import SellerModel,ProductModel,CustomerModel,BidsModel
class SellerSerializer(ModelSerializer):
    class Meta:
        model=SellerModel
        fields='__all__'

class ProductSerializer(ModelSerializer):
    class Meta:
        model=ProductModel
        fields='__all__'

class CustomerSerializer(ModelSerializer):
    class Meta:
        model=CustomerModel
        fields='__all__'


class BidsSerializer(ModelSerializer):
    class Meta:
        model=BidsModel
        fields='__all__'
