from django.db import models

class Cotegory(models.Model):
    cotegory_name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.cotegory_name

class Product(models.Model):
    product_name = models.CharField(max_length=32)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cotegory = models.ForeignKey(Cotegory, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    have = models.BooleanField(default=True)
    video = models.FileField(upload_to='videos', null=True, blank=True)

    def __str__(self):
        return self.product_name

class ProductPhotos(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img/')
