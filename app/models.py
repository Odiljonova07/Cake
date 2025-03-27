from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='cake/')
    countProducts = models.IntegerField()

    def __str__(self):
        return self.name

class Cake(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='cake/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.IntegerField()
    isDiscount = models.IntegerField(null=True, blank=True)
    info_number = models.JSONField(default=list) 
    

    def discounted_price(self):
        if self.isDiscount and self.isDiscount > 0:
            return self.price - (self.isDiscount * self.price / 100)
        return self.price  

    def __str__(self):
        return self.name