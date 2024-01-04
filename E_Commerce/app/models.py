from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.db.models.signals import pre_save

from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_vendor = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email

    

# Create your models here.

#HOME PAGE
class slider(models.Model):
    DISCOUNT_DEAL = (               # for Discount_deal choices
        ('HOT DEAL', 'HOT DEAL'),
        ('New Arrivals','New Arrivals')
    )
    Image = models.ImageField(upload_to='media/slider_imgs')
    Discount_Deal = models.CharField(choices=DISCOUNT_DEAL,max_length=100)
    SALE = models.IntegerField()
    Brand_Name = models.CharField(max_length=200)
    Discount = models.IntegerField()
    Link = models.CharField(max_length=200)

    def __str__(self):
        return self.Brand_Name
    
    
class banner_area(models.Model):
    Image = models.ImageField(upload_to='media/banner_img')
    Discount_Deal = models.CharField(max_length=100)
    Quote = models.CharField(max_length=100)
    Discount = models.IntegerField()
    Link = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.Quote
    

# MENU BAR CATAGORY
class Main_Catagory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Catagory(models.Model):
    main_catagory = models.ForeignKey(Main_Catagory,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name + " -- " + self.main_catagory.name

class Sub_Catagory(models.Model):
    catagory = models.ForeignKey(Catagory,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.catagory.main_catagory.name + ' -- ' + self.catagory.name + ' -- ' + self.name
    

# PRODUCT DETAIL SECTION
class Section(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    
    total_quantity = models.IntegerField()
    Availability = models.IntegerField()
    featured_image = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    tax = models.IntegerField(null=True)
    packing_cost = models.IntegerField(null=True)
    Discount = models.IntegerField()
    Product_Information = RichTextField()
    model_Name = models.CharField(max_length=50)
    Catagorys = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    Tags = models.CharField(max_length=100)
    Description = RichTextField()
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)

    def __str__(self):
        return self.product_name
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("product_detail", kwargs={'slug': self.slug})

    class Meta:
        db_table = "app_Product"

def create_slug(instance, new_slug=None):
    slug = slugify(instance.product_name)
    if new_slug is not None:
        slug = new_slug
    qs = Product.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, Product)



class Product_Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Image_url = models.CharField(max_length=200)

class Additional_Information(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    specification = models.CharField(max_length=100)
    detail = models.CharField(max_length=100)


class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True) 
    packaged = models.BooleanField(default=False)
    dispatched = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product_name
    
class NegotiationPannel(models.Model):
    name = models.CharField(max_length=100)
    offerprice = models.IntegerField()
    product_value = models.IntegerField()
    STATUS_CHOICES = [
        ('PENDING', 'PENDING'),
        ('ACCEPTED', 'ACCEPTED'),
        ('REJECTED', 'REJECTED'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return self.name