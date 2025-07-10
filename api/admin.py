from django.contrib import admin
from .models import User, Product, Tag, Offer, ProductImage, ProductVideo, Order, OrderItem, Cart, CartItem, Wishlist, WishlistItem, OTP, Country
from .utils import upload_file_to_spaces
from django.utils.html import format_html
from django import forms
from dotenv import load_dotenv
import os

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = '__all__'
        help_texts = {
            'alt_text': 'If left empty, will auto-fill with product name when saved.'
        }

class ProductImageAdmin(admin.ModelAdmin):
    form = ProductImageForm
    list_display = ("id", "image_preview", "alt_text_link", "product_link")
    readonly_fields = ("image_preview",)
    search_fields = ['alt_text', 'product__name']

    def alt_text_link(self, obj):
        from django.urls import reverse
        url = reverse('admin:api_productimage_change', args=[obj.pk])
        alt_text = obj.alt_text if obj.alt_text else "No Alt Text"
        return format_html('<a href="{}">{}</a>', url, alt_text)
    alt_text_link.short_description = "Alt Text"

    def product_link(self, obj):
        from django.urls import reverse
        url = reverse('admin:api_product_change', args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', url, obj.product.name)
    product_link.short_description = "Product"

    def image_preview(self, obj):
        if obj.image:
            url = obj.image
            return format_html('<img src="{}" style="max-height: 200px; max-width: 200px;" />', str(url))
        return "No Image"
    image_preview.short_description = "Image Preview"

    def save_model(self, request, obj, form, change):
        if not obj.alt_text and obj.product:
            obj.alt_text = obj.product.name
        load_dotenv()
        if 'image' in form.changed_data and obj.image:
            url = upload_file_to_spaces(obj.image.file, object_name=f"{obj.image.name}")
            cdn_base = os.environ.get('DO_SPACES_CDN')
            filename = os.path.basename(url)
            obj.image = f"{cdn_base}/magnificentfox/{filename}"
        super().save_model(request, obj, form, change)

class ProductVideoAdmin(admin.ModelAdmin):
    list_display = ("id", "video",)
    search_fields = ['title', 'product__name']

    def save_model(self, request, obj, form, change):
        if 'video' in form.changed_data and obj.video:
            url = upload_file_to_spaces(obj.video.file, object_name=f"{obj.video.name}")
            print(f"[DEBUG] upload_file_to_spaces returned: {url}")
            obj.video = url
        super().save_model(request, obj, form, change)

class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['tags', 'offers', 'images', 'videos', 'countries']

class TagAdmin(admin.ModelAdmin):
    search_fields = ['name']

class OfferAdmin(admin.ModelAdmin):
    search_fields = ['name']

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'is_active')
    search_fields = ['name', 'code']
    list_filter = ['is_active']

class UserAdmin(admin.ModelAdmin):
    autocomplete_fields = ['country']
    search_fields = ['name', 'email', 'mobile']

admin.site.register(User, UserAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Wishlist)
admin.site.register(WishlistItem)
admin.site.register(OTP)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(ProductVideo, ProductVideoAdmin)

admin.site.site_header = "Magnificent Fox Administration"
admin.site.site_title = "Magnificent Fox Admin Portal"
admin.site.index_title = "Welcome to the Magnificent Fox Admin"
