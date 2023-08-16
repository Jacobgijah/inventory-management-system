from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20, null=True)
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class Store(models.Model):
    name = models.CharField(max_length=50, null=True)
    department = models.CharField(max_length=100, null=True)
    building = models.CharField(max_length=100, null=True)
    room = models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=20, null=True)
    class Meta:
        verbose_name_plural = 'Brand'

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=50, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=100, null=True)
    quantity = models.PositiveIntegerField(null=True)
    price = models.FloatField(null=True)
      
    def __str__(self):
        return self.name