from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SellerSerializer,ProductSerializer,CustomerSerializer,BidsSerializer
from .models import SellerModel,ProductModel,CustomerModel,BidsModel
from .exceptions import IdNotAvailable,InvalidData,IdOrDateNotAvailable,ProductNotAvailable
from django.http import HttpResponse
import rest_framework
class SellerView(APIView):
    def get(self,request,pk=None,format=None):
        #Write the logic here
        return HttpResponse(status=rest_framework.status.HTTP_204_NO_CONTENT)

    def post(self, request,format=None):
        #Write the logic here
        return HttpResponse(status=rest_framework.status.HTTP_204_NO_CONTENT)

    def delete(self,request,pk,format=None):
        #Write the logic here
        return HttpResponse(status=rest_framework.status.HTTP_204_NO_CONTENT)

class ProductView(APIView):
    def get(self,request,pk=None,format=None):
        #Write the logic here
        return HttpResponse(status=rest_framework.status.HTTP_204_NO_CONTENT)

    def post(self, request,format=None):
        #Write the logic here
        return HttpResponse(status=rest_framework.status.HTTP_204_NO_CONTENT)

    def delete(self,request,pk,format=None):
        #Write the logic here
        return HttpResponse(status=rest_framework.status.HTTP_204_NO_CONTENT)



class GetProductView(APIView):
    def get(self,request,pk=None,format=None):
        #Write the logic here
        return HttpResponse(status=rest_framework.status.HTTP_204_NO_CONTENT)

class ListProductsByCategoryView(APIView):
    def get(self,request,pk=None,format=None):
        #Write the logic here
        return HttpResponse(status=rest_framework.status.HTTP_204_NO_CONTENT)


class CustomerView(APIView):
    def get(self,request,pk=None,format=None):
        #Write the logic here
        return HttpResponse(status=rest_framework.status.HTTP_204_NO_CONTENT)
    def post(self, request,format=None):
        #Write the logic here
        return HttpResponse(status=rest_framework.status.HTTP_204_NO_CONTENT)
    def put(self,request,pk,format=None):
        #Write the logic here
        return HttpResponse(status=rest_framework.status.HTTP_204_NO_CONTENT)

    def patch(self,request,pk,format=None):
        #Write the logic here
        return HttpResponse(status=rest_framework.status.HTTP_204_NO_CONTENT)

class BidsView(APIView):
    def get(self,request,pk=None,format=None):
        #Write the logic here
        return HttpResponse(status=rest_framework.status.HTTP_204_NO_CONTENT)

    def post(self, request,format=None):
        #Write the logic here
        return HttpResponse(status=rest_framework.status.HTTP_204_NO_CONTENT)

class BidsByDateView(APIView):
    def get(self,request,pk=None,format=None):
        #Write the logic here
        return HttpResponse(status=rest_framework.status.HTTP_204_NO_CONTENT)
