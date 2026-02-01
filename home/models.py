from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
class Food_And_Drinks(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='cat')
    name = models.CharField(max_length=50)
    pic = models.ImageField(upload_to='product/')
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name