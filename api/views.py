from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import User, Product, Order, Tag, ProductImage, ProductVideo, WishlistItem, EditorialPick, Country
from .serializers import UserSerializer, ProductSerializer, OrderSerializer, ColumnStructureSerializer, CountrySerializer

# Generic Views for CRUD Operations
class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProductListCreate(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        queryset = Product.objects.all()
        tags = self.request.query_params.get('tags')
        country = self.request.query_params.get('country')
        
        if tags:
            tag_names = [tag.strip() for tag in tags.split(',') if tag.strip()]
            queryset = queryset.filter(tags__name__in=tag_names).distinct()
        
        if country:
            queryset = queryset.filter(countries__code__iexact=country).distinct()
        
        return queryset


class OrderListCreate(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class CountryListCreate(generics.ListCreateAPIView):
    queryset = Country.objects.filter(is_active=True)
    serializer_class = CountrySerializer

# API Endpoint for Reviews Data
@api_view(['GET'])
def reviews_data(request):
    """Returns reviews data from database"""
    products = Product.objects.exclude(customer_reviews__isnull=True).exclude(customer_reviews='')
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
