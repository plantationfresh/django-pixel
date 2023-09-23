from django.db import models

# Create your models here.
class product(models.Model):

    name = models.CharField(max_length=20)
    variant = models.CharField(max_length=20)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + "_" + self.variant

class product_price(models.Model):

    product = models.ForeignKey(product, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
