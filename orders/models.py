from django.db import models
from users.models import UserProfile
from products.models import ProductModel

class OrderModel(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    products = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='product_order')
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.price = self.products.price * self.amount
        super(OrderModel, self).save(*args, **kwargs)

