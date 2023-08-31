from django.db import models
from dashboard.models import Item
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(null=True)
    issued_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=10,  default='Pending',null=True)
    
    class Meta:
        ordering = ['-issued_date']
    
    def __str__(self):
        return f'{self.item.name}-{self.quantity}'
