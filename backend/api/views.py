from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer
# Create your views here.

@api_view(["GET","POST"])
def home(request, *args, **kwargs):
    if request.method=="GET":
        instance = Product.objects.all().order_by("?").first()
        data = {}
        if instance:
            serialized = ProductSerializer(instance)
        return Response(serialized.data)

    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            print(serializer.data)
            return Response(serializer.data)
        return Response({"Invalid":"Data is invalid"},status=400)



