from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SellerSerializer,ProductSerializer,CustomerSerializer,BidsSerializer
from .models import SellerModel,ProductModel,CustomerModel,BidsModel
from .exceptions import IdNotAvailable,InvalidData,IdOrDateNotAvailable,ProductNotAvailable

#from rest_framework.generics import ListAPIView
#from .service import NotesService

#Seller
class SellerView(APIView):
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            qs=SellerModel.objects.filter(seller_id=id)
            if qs:
                serializer=SellerSerializer(qs,many=True)
                return Response(serializer.data)
            else:
                raise IdNotAvailable()
        qs=SellerModel.objects.all()
        serializer=SellerSerializer(qs,many=True)
        return Response(serializer.data)

    def post(self, request,format=None):
        serializer=SellerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Seller Registered"},status=status.HTTP_201_CREATED)
        raise InvalidData()
        #return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        #id=pk
        qs=SellerModel.objects.filter(seller_id=pk).delete()
        if qs[0]==1:
            return Response({"msg":"Seller deleted"})
        raise IdNotAvailable()



#Product
class ProductView(APIView):
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            qs=ProductModel.objects.filter(product_id=id)
            if qs:
                serializer=ProductSerializer(qs,many=True)
                return Response(serializer.data)
            else:
                raise IdNotAvailable()
        qs=ProductModel.objects.all()
        serializer=ProductSerializer(qs,many=True)
        return Response(serializer.data)

    def post(self, request,format=None):
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Product added"},status=status.HTTP_201_CREATED)
        raise InvalidData()
        #return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        #id=pk
        qs=ProductModel.objects.filter(product_id=pk).delete()
        if qs[0]==1:
            return Response({"msg":"Product deleted"})
        raise IdNotAvailable()



class GetProductView(APIView):
    def get(self,request,pk=None,format=None):
        seller_id=self.request.GET.get('seller_id')
        #id=pk
        #if id is not None:
        qs=ProductModel.objects.filter(seller_id=seller_id)
        #print(qs)
        if qs:
            serializer=ProductSerializer(qs,many=True)
            return Response(serializer.data)
        else:
            raise IdNotAvailable()
        # qs=ProductModel.objects.all()
        # serializer=ProductSerializer(qs,many=True)
        # return Response(serializer.data)

class ListProductsByCategoryView(APIView):
    def get(self,request,pk=None,format=None):
        customer_id=self.request.GET.get('customer_id')
        product_category=self.request.GET.get('product_category')
        qs=CustomerModel.objects.filter(customer_id=customer_id)
        if qs:
            product_qs=ProductModel.objects.filter(product_category=product_category)
            bids_qs=BidsModel.objects.all()
            product_serializer=ProductSerializer(product_qs,many=True)
            bids_serializer=BidsSerializer(bids_qs,many=True)
            L=[]
            for bids in bids_serializer.data:
                for product in product_serializer.data:
                    if  bids['product_id']==product['product_id']:
                        L.append(bids)
            return Response(L)
        else:
            raise IdNotAvailable()


    # def get(self,request,pk=None,format=None):#How to filter 2 querysets
    #     customer_id=self.request.GET.get('customer_id')
    #     product_category=self.request.GET.get('product_category')
    #     qs=CustomerModel.objects.filter(customer_id=customer_id)
    #     if qs:
    #         qs=ProductModel.objects.filter(product_category=product_category)
    #
    #         if qs:
    #             serializer=ProductSerializer(qs,many=True)
    #             return Response(serializer.data)
    #         else:
    #             raise ProductNotAvailable()
    #     else:
    #         raise IdNotAvailable()

#Customer
class CustomerView(APIView):
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            qs=CustomerModel.objects.filter(customer_id=id)
            if qs:
                serializer=CustomerSerializer(qs,many=True)
                return Response(serializer.data)
            else:
                raise IdNotAvailable()
        qs=CustomerModel.objects.all()
        serializer=CustomerSerializer(qs,many=True)
        return Response(serializer.data)
    def post(self, request,format=None):
        serializer=CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Customer Registered"},status=status.HTTP_201_CREATED)
        raise InvalidData()
        #return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk,format=None):
        id=pk
        try:
            note=CustomerModel.objects.get(customer_id=id)
            serializer=CustomerSerializer(note,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg":"Customer updated"})
        except CustomerModel.DoesNotExist:
            raise IdNotAvailable()
        raise InvalidData()
        #return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk,format=None):
        try:
            note=CustomerModel.objects.get(customer_id=pk)
            serializer=CustomerSerializer(note,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg":"Partial Customer data updated"})
        except CustomerModel.DoesNotExist:
            raise IdNotAvailable()
        raise InvalidData()
        #return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



#Bids
class BidsView(APIView):
    def get(self,request,pk=None,format=None):
        #id=pk
        product_id=self.request.GET.get('product_id')
        qs=BidsModel.objects.filter(product_id=product_id)
        if qs:
            serializer=BidsSerializer(qs,many=True)
            return Response(serializer.data)
        else:
            raise IdNotAvailable()

    def post(self, request,format=None):
        customer_id=self.request.GET.get('customer_id')
        product_id=self.request.GET.get('product_id')
        qs=CustomerModel.objects.filter(customer_id=customer_id)
             #qs = NotesService.search_by_id(id)
        if qs:
            qs=ProductModel.objects.filter(product_id=product_id)
            if qs:
                serializer=BidsSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"msg":"Placed bid on a product successfully"},status=status.HTTP_201_CREATED)
                raise InvalidData()
            else:
                raise IdNotAvailable()
        else:
            raise IdNotAvailable()

class BidsByDateView(APIView):
    def get(self,request,pk=None,format=None):
        #id=pk
        product_id=self.request.GET.get('product_id')
        bidding_date=self.request.GET.get('bidding_date')
        qs=BidsModel.objects.filter(product_id=product_id,bidding_date=bidding_date)
        if qs:
            serializer=BidsSerializer(qs,many=True)
            return Response(serializer.data)
        else:
            raise IdOrDateNotAvailable()


#Filtering
# class SearchNotesByIdView(ListAPIView):
#     serializer_class =NotesSerializer
#     def get_queryset(self):
#         id=self.request.GET.get('id')#getting field value from url
#         if id is not None:
#             qs = NotesService.search_by_id(id)
#             if qs:
#                 return qs
#             else:
#                 raise IdNotAvailable()
#
# class SearchNotesByAuthorView(ListAPIView):
#     serializer_class =NotesSerializer
#     def get_queryset(self):
#         name=self.request.GET.get('author')
#         if name is not None:
#             qs = NotesService.search_by_author(name)
#             if qs:
#                 return qs
#             else:
#                 raise AuthorNotAvailable()
#
# class SearchNotesByStatusView(ListAPIView):
#     serializer_class =NotesSerializer
#     def get_queryset(self):
#         status=self.request.GET.get('status')
#         if status is not None:
#             qs = NotesService.search_by_status(status)
#             if qs:
#                 return qs
#             else:
#                 raise StatusNotAvailable()
