from django.contrib import admin
from .models import User, Product, Tag, Offer, ProductImage, ProductVideo, Order, OrderItem, Cart, CartItem, Wishlist, WishlistItem, OTP
from .utils import upload_file_to_spaces
from django.utils.html import format_html
from dotenv import load_dotenv
import os

class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "image_preview")
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            url = obj.image
            return format_html('<img src="{}" style="max-height: 200px; max-width: 200px;" />', str(url))
        return "No Image"
    image_preview.short_description = "Preview"

    def save_model(self, request, obj, form, change):
        load_dotenv()
        if 'image' in form.changed_data and obj.image:
            url = upload_file_to_spaces(obj.image.file, object_name=f"{obj.image.name}")
            cdn_base = os.environ.get('DO_SPACES_CDN')
            filename = os.path.basename(url)
            obj.image = f"{cdn_base}/magnificentfox/{filename}"
        super().save_model(request, obj, form, change)

class ProductVideoAdmin(admin.ModelAdmin):
    list_display = ("id", "video",)

    def save_model(self, request, obj, form, change):
        if 'video' in form.changed_data and obj.video:
            url = upload_file_to_spaces(obj.video.file, object_name=f"{obj.video.name}")
            print(f"[DEBUG] upload_file_to_spaces returned: {url}")
            obj.video = url
        super().save_model(request, obj, form, change)

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Offer)
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
