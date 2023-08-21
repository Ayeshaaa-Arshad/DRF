from django.db import models

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=10)
    description=models.TextField(blank=True,null=True)
    price=models.DecimalField(max_digits=20,decimal_places=3,default=0.0)
