from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SellerSerializer,ProductSerializer,CustomerSerializer,BidsSerializer
from .models import SellerModel,ProductModel,CustomerModel,BidsModel
from .exceptions import IdNotAvailable,InvalidData,IdOrDateNotAvailable,ProductNotAvailable

class SellerView(APIView):
    def get(self,request,pk=None,format=None):
        #Write the logic here
        return Response({})

    def post(self, request,format=None):
        #Write the logic here
        return Response({})

    def delete(self,request,pk,format=None):
        #Write the logic here
        return Response({})

class ProductView(APIView):
    def get(self,request,pk=None,format=None):
        #Write the logic here
        return Response({})

    def post(self, request,format=None):
        #Write the logic here
        return Response({})

    def delete(self,request,pk,format=None):
        #Write the logic here
        return Response({})



class GetProductView(APIView):
    def get(self,request,pk=None,format=None):
        #Write the logic here
        return Response({})

class ListProductsByCategoryView(APIView):
    def get(self,request,pk=None,format=None):
        #Write the logic here
        return Response({})


class CustomerView(APIView):
    def get(self,request,pk=None,format=None):
        #Write the logic here
        return Response({})
    def post(self, request,format=None):
        #Write the logic here
        return Response({})
    def put(self,request,pk,format=None):
        #Write the logic here
        return Response({})

    def patch(self,request,pk,format=None):
        #Write the logic here
        return Response({})

class BidsView(APIView):
    def get(self,request,pk=None,format=None):
        #Write the logic here
        return Response({})

    def post(self, request,format=None):
        #Write the logic here
        return Response({})

class BidsByDateView(APIView):
    def get(self,request,pk=None,format=None):
        #Write the logic here
        return Response({})
