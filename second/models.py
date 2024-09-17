from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class category(models.Model):
    category_name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    
    def __str__(self):
        return self.category_name

class product(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='logo/%Y/%m/%d/', blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class product2(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image2 = models.ImageField(upload_to='logo/%Y/%m/%d/', blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name    

class asettings(models.Model):
    a_name=models.CharField(max_length=100)
    a_logo=models.ImageField(upload_to='',blank=True,null=True)
    a_email=models.EmailField(max_length=100,unique=True)
    a_phone=models.CharField(max_length=100)

    def __str__(self):
        return self.a_name
    
class ad(models.Model):


    adname=models.CharField(max_length=100)
    addlogo=models.ImageField(upload_to='logo/%Y/%m/%d/',blank=True,null=True)

class agx(models.Model):
    agxname=models.CharField(max_length=100)
    agxlogo=models.ImageField(upload_to='logo/%Y/%m/%d/',blank=True,null=True)

class fo(models.Model):
    foname=models.CharField(max_length=100)
    fologo=models.ImageField(upload_to='logo/%Y/%m/%d/',blank=True,null=True)
    foprice=models.IntegerField()


class review(models.Model):

    re_name=models.CharField(max_length=100)
    re_logo=models.ImageField(upload_to='logo/%Y/%m/%d/',blank=True,null=True)
    re_prof=models.CharField(max_length=100)
    re_dep=models.TextField()

class footer(models.Model):
    footaddress=models.CharField(max_length=100)
    footemail=models.EmailField(unique=True)
    footph=models.IntegerField()
    we=models.ImageField(upload_to='',blank=True,null=True)
    we1=models.ImageField(upload_to='',blank=True,null=True)
    we2=models.ImageField(upload_to='',blank=True,null=True)
    we3=models.ImageField(upload_to='',blank=True,null=True)

class two(models.Model):
    twon=models.CharField(max_length=100)
    twoim=models.ImageField(upload_to='',blank=True,null=True)
    twopr=models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return self.twon

class cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(two, through='CartItem')

class CartItem(models.Model):

    cart = models.ForeignKey(cart, on_delete=models.CASCADE)
    product = models.ForeignKey(two, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(two, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s wishlist"