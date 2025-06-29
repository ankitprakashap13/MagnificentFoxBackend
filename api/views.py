from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import User, Product, Order, Tag, ProductImage, ProductVideo, WishlistItem, EditorialPick
from .serializers import UserSerializer, ProductSerializer, OrderSerializer, ColumnStructureSerializer

# Generic Views for CRUD Operations
class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderListCreate(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# API Endpoint for Column Structure Data
@api_view(['GET'])
def column_structure_data(request):
    """Returns API status message"""
    data = {"message": "API is working!"}
    serializer = ColumnStructureSerializer(data)
    return Response(serializer.data)

# API Endpoint to List Products
@api_view(['GET'])
def list_products(request):
    """Returns a list of products with their details"""
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

# API Endpoint for Card List Data
@api_view(['GET'])
def card_list_data(request):
    """Returns card list data from database"""
    tags = Tag.objects.all()
    data = [{'title': tag.name, 'onClick': f'/collections/{tag.name.lower().replace(" ", "-")}'} for tag in tags]
    return Response(data)

# API Endpoint for Favourites Data
@api_view(['GET'])
def favourites_data(request):
    """Returns editorial picks and favourites data from database"""
    products = Product.objects.filter(is_editorial_pick=True)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

# API Endpoint for Reviews Data
@api_view(['GET'])
def reviews_data(request):
    """Returns reviews data from database"""
    products = Product.objects.exclude(customer_reviews__isnull=True).exclude(customer_reviews='')
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

# API Endpoint for Video Cards Data
@api_view(['GET'])
def video_cards_data(request):
    """Returns video cards data from database"""
    videos = ProductVideo.objects.all()
    products = [video.product for video in videos]
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
