from django.db import models

# Create your models here.
CATEGORY = (
    ('hardware', 'hardware'),
    ('software', 'software'),
)

class Brand(models.Model):
    name = models.CharField(max_length=20, null=True)
    description = models.TextField(null=True)
    class Meta:
        verbose_name_plural = 'Brand'

    def __str__(self):
        return self.name   

class Attribute(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    model_name = models.CharField(max_length=20, null=True)
    generation = models.PositiveBigIntegerField(null=True)
    attribute_type = models.CharField(max_length=20, null=True)
    manufacture_year = models.DateField(null=True)  
    class Meta:
        verbose_name_plural = 'Attribute'

    def __str__(self):
        return f'{self.brand}-{self.model_name}' 

class Store(models.Model):
    name = models.CharField(max_length=50, null=True)
    building = models.CharField(max_length=100, null=True)
    room = models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=50, null=True)
    brand = models.ForeignKey(Attribute, on_delete=models.CASCADE, null=True)
    serial_no = models.CharField(max_length=11, null=True)
    imei = models.PositiveIntegerField(null=True)
    category = models.CharField(max_length=10, choices=CATEGORY, null=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True)
    quantity = models.PositiveIntegerField(null=True)
    warranty = models.DateField(null=True)
    registered_date = models.DateField(auto_now=True,null=True)
    expiry_date = models.DateField(null=True) # optional field
    price = models.FloatField(null=True)
      
    def __str__(self):
        return self.name