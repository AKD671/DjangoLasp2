from email.policy import default
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
# Create your models here.
class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(isactive=True)


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)


    class Meta:
        verbose_name_plural = 'catagories'

    def get_absolute_url(self):
        return reverse("store:category_list", args=[self.slug])
    

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey( User, on_delete=models.CASCADE, related_name= 'product_creator')
    title = models.CharField(max_length=255)
    author = models.CharField(default='', max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(default='0', max_digits=5, decimal_places=2)
    instock = models.BooleanField(default=True)
    isactive = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    products = ProductManager()


    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'Products'
    def get_absolute_url(self):
        return reverse("store:product_detail", args=[self.slug])
    
    def __str__(self):
        return self.title
    
