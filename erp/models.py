from django.db import models

# Create your models here.
class Product(models.Model):
    class Meta:
        db_table = "products"
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('F', 'Free'),
    )
    size = models.CharField(choices=sizes, max_length=1)


    def __str__(self):
        return self.code


class Inbound(models.Model):
    class Meta:
        db_table = "inbound"

    code = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    inbound_date = models.DateField(auto_now=True)
    price = models.IntegerField()
    sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('F', 'Free'),
    )
    size = models.CharField(choices=sizes, max_length=1)

class Outbound(models.Model):
    class Meta:
        db_table = "outbound"

    code = models.ForeignKey(Product, on_delete=models.CASCADE)
    out_quantity = models.IntegerField()
    outbound_date = models.DateField(auto_now=True)
    price = models.IntegerField()
    sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('F', 'Free'),
    )
    size = models.CharField(choices=sizes, max_length=1)

class Inventory(models.Model):
    class Meta:
        db_table = "inventory"

    code = models.ForeignKey(Product, on_delete=models.CASCADE)
    total_quantity = models.IntegerField()
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    size = models.CharField(max_length=1)
