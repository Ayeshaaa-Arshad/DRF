from rest_framework import serializers
from products.models import Product
from products.validators import validate_title,unique_product_title

class ProductSerializer(serializers.ModelSerializer):
    my_discount=serializers.SerializerMethodField(read_only=True)
    title=serializers.CharField(validators=[unique_product_title])
    class Meta:
        model=Product
        fields=['id','title','description','price','sale_price','my_discount']

    def get_my_discount(self,obj):
        return obj.get_discount()
