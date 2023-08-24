from products.models import Product
from rest_framework import generics,mixins
from products.serializers import ProductSerializer
from rest_framework.response import Response
from api.mixins import StaffEditorPermissionMixin
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
# Create your views here.

class ProductDetailView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'

# class ProductCreateView(generics.ListAPIView):
#     queryset=Product.objects.all()
#     serializer_class=ProductSerializer
#
#     def perform_create(self,serializer):#if want to add additional data
#         title=serializer.validated_data.get('title')
#         title='Android'
#         serializer.validated_data['extra_field'] = 'Some additional value'
#         serializer.save(title=title,description=title)
class ProductCreateView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    # def perform_create(self,serializer):             #if want to add additional data
    #     title=serializer.validated_data.get('title')
    #     title='Android'
    #     serializer.save(title=title,description=title)

class ProductListView(StaffEditorPermissionMixin,generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class ProductUpdateView(StaffEditorPermissionMixin,generics.UpdateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer


class ProductDeleteView(StaffEditorPermissionMixin,generics.DestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class ProductAltView(APIView):
    def get(self,request,pk=None,*args,**kwargs):
        if pk:
            product = get_object_or_404(Product, pk=pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        obj=Product.objects.all()
        if obj:
            serializer=ProductSerializer(obj,many=True)
            return Response(serializer.data)
    def post(self,request,*args,**kwargs):
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

class ProductMixinView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    def get(self,request,*args,**kwargs):
        pk=kwargs.get("pk")
        if pk:
            return self.retrieve(request,*args,**kwargs)
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


