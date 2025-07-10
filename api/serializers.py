from rest_framework import serializers
from .models import User, Product, Order, OrderItem, Country, Tag, Offer, ProductImage, ProductVideo

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name', 'code', 'is_active']

class UserSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'name', 'email', 'mobile', 'dob', 'gender', 'country']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ['id', 'name', 'discount_percentage', 'start_date', 'end_date']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'alt_text']

class ProductVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVideo
        fields = ['id', 'video', 'title']

class ProductSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    countries = CountrySerializer(many=True, read_only=True)
    offers = OfferSerializer(many=True, read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    videos = ProductVideoSerializer(many=True, read_only=True)
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'mrp', 'discount_percentage', 'inclusive_of_taxes', 'sizes', 'quantity', 'dispatch_time', 'cash_on_delivery', 'return_policy', 'details', 'design_and_fit', 'fabric_and_care', 'customer_reviews', 'created_at', 'updated_at', 'tags', 'countries', 'offers', 'images', 'videos']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'created_at', 'updated_at', 'total_price', 'status', 'order_items']

class ColumnStructureSerializer(serializers.Serializer):
    message = serializers.CharField()