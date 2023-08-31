from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=20, null=True)
    description = models.TextField(null=True)
    class Meta:
        verbose_name_plural = 'Brand'

    def __str__(self):
        return self.name   

class Attribute(models.Model):
    model_name = models.CharField(max_length=20, null=True)
    generation = models.PositiveBigIntegerField(null=True)
    attribute_type = models.CharField(max_length=20, null=True)
    manufacture_year = models.DateField(null=True)  
    class Meta:
        verbose_name_plural = 'Attribute'

    def __str__(self):
        return f'{self.model_name}-{self.generation}' 

class Store(models.Model):
    name = models.CharField(max_length=50, null=True)
    building = models.CharField(max_length=100, null=True)
    room = models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return self.name

class Item(models.Model):
    CATEGORY = (
        ('hardware', 'Hardware'),
        ('software', 'Software'),
        ('other', 'Other'),
    )

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    model_name = models.ForeignKey(Attribute, on_delete=models.CASCADE, null=True)
    serial_no = models.CharField(max_length=11, null=True)
    imei = models.PositiveIntegerField(null=True)
    category = models.CharField(max_length=10, choices=CATEGORY, null=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True)
    quantity = models.PositiveIntegerField(null=True)
    receive_quantity = models.PositiveIntegerField(default='0', null=True, blank=True)
    warranty = models.DateField(null=True)
    registered_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    price = models.FloatField(null=True)
    remarks = models.CharField(max_length=50, null=True)
    class Meta:
        ordering = ['-registered_date']
    
    def __str__(self):
        return f'{self.name}: {self.brand.name}-{self.model_name.model_name}'