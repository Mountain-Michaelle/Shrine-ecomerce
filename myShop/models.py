from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    #get absolut url declaration 
    def get_absolute_url(self):
        return reverse('myShop:product_list_by_category', 
        args=[self.slug])


    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('-name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        

    def __str__(self):
        return self.name

class Product(models.Model):
    #Get absolute url fuctionality declaration 
    def get_absolute_url(self):
        return reverse('myShop:product_detail',
        args=[self.id, self.slug])

    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True, db_index=True)
    image1 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image2 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image3 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)

    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together=(('id', 'slug'),)

    def __str__(self):
        return self.name
        
