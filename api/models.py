from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db.models.signals import post_save
from django.dispatch import receiver
from dotenv import load_dotenv
import os

load_dotenv()
get_env = lambda key, default=None: os.getenv(key, default)

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=255)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True, blank=True)
    groups = models.ManyToManyField(
        Group,
        related_name='api_user_set',  # Add related_name to avoid clash
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='api_user_permissions_set',  # Add related_name to avoid clash
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    REQUIRED_FIELDS = ['name', 'mobile', 'password']
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mrp = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Fix typo here
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    inclusive_of_taxes = models.BooleanField(default=True)
    sizes = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    dispatch_time = models.CharField(max_length=255, null=True, blank=True)
    cash_on_delivery = models.BooleanField(default=True)
    return_policy = models.CharField(max_length=255, null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    design_and_fit = models.TextField(null=True, blank=True)
    fabric_and_care = models.TextField(null=True, blank=True)
    customer_reviews = models.TextField(null=True, blank=True)
    is_editorial_pick = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Tag', related_name='products', blank=True)
    offers = models.ManyToManyField('Offer', related_name='products', blank=True)
    images = models.ManyToManyField('ProductImage', related_name='products', blank=True)
    videos = models.ManyToManyField('ProductVideo', related_name='products', blank=True)
    countries = models.ManyToManyField('Country', related_name='products', blank=True)
    
    def __str__(self):
        return self.name


class OTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=3, unique=True, help_text='ISO country code (e.g., US, IN, UK)')
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = 'Countries'
    
    def __str__(self):
        return self.name


class Offer(models.Model):
    name = models.CharField(max_length=255)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    
    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    image = models.URLField(max_length=2048)
    alt_text = models.CharField(max_length=255, blank=True, help_text='Alternative text for accessibility')
    
    def __str__(self):
        return f'{self.product.name} - Image {self.id}' if self.alt_text == '' else self.alt_text

class ProductVideo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_videos')
    video = models.FileField(upload_to='product_videos/', null=True, blank=True)
    title = models.CharField(max_length=255, blank=True, help_text='Video title or description')
    
    def __str__(self):
        return f'{self.product.name} - Video {self.id}' if self.title == '' else self.title

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default='Pending')
    
    def __str__(self):
        return f'Order #{self.id} - {self.user.name}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wishlist')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE, related_name='wishlist_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class EditorialPick(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ('product',)

@receiver(post_save, sender=ProductVideo)
def add_has_video_tag(sender, instance, created, **kwargs):
    if created and instance.video:
        has_video_tag, _ = Tag.objects.get_or_create(name='HAS-VIDEO')
        instance.product.tags.add(has_video_tag)

