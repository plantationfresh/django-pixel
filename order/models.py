from django.db import models
from pos.models import product
# Create your models here.
class order(models.Model):

    order_id = models.IntegerField()
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    customer = models.CharField(max_length=20, default="NA")
    type = models.CharField(max_length=20)
    quantity = models.IntegerField()
    total = models.FloatField()

    def __str__(self):
        return str(self.order_id) + "_" + str(self.product)
