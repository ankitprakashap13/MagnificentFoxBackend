import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MagnificentFox.settings')
django.setup()

from api.models import Tag, Product, ProductImage, ProductVideo
from decimal import Decimal

def create_dummy_data():
    # Create Tags
    tags_data = [
        'PAJAMA SETS', 'SHORT SETS', 'BOTTOMS', 'T-SHIRTS', 
        'LINEN TOPS', 'LOUNGE PANTS', 'CO-ORD SETS'
    ]
    
    for tag_name in tags_data:
        tag, created = Tag.objects.get_or_create(name=tag_name)
        if created:
            print(f"Created tag: {tag_name}")
    
    # Create Products
    products_data = [
        {
            'name': 'Coral Rose Lucy Butter-Soft Cotton Knit Women\'s Pajama Set',
            'description': 'Comfortable and stylish pajama set made from butter-soft cotton',
            'price': Decimal('2799.00'),
            'mrp': Decimal('2999.00'),
            'discount_percentage': Decimal('6.67'),
            'customer_reviews': 'Amazing quality and super comfortable. Perfect fit!',
            'is_editorial_pick': True
        },
        {
            'name': 'Ivy Blue Floral Cotton Blend Women\'s Pajama Set',
            'description': 'Beautiful floral pattern pajama set in cotton blend fabric',
            'price': Decimal('2999.00'),
            'mrp': Decimal('3200.00'),
            'discount_percentage': Decimal('6.28'),
            'customer_reviews': 'Love the floral design. Very comfortable for sleeping.',
            'is_editorial_pick': True
        },
        {
            'name': 'Classic White Cotton T-Shirt',
            'description': 'Basic white cotton t-shirt for everyday wear',
            'price': Decimal('899.00'),
            'mrp': Decimal('1199.00'),
            'discount_percentage': Decimal('25.02'),
            'customer_reviews': 'Great quality cotton. Fits perfectly and washes well.',
            'is_editorial_pick': False
        },
        {
            'name': 'Summer Linen Lounge Pants',
            'description': 'Breathable linen pants perfect for summer lounging',
            'price': Decimal('1599.00'),
            'mrp': Decimal('1899.00'),
            'discount_percentage': Decimal('15.80'),
            'customer_reviews': 'Very breathable and comfortable. Perfect for hot weather.',
            'is_editorial_pick': True
        }
    ]
    
    for product_data in products_data:
        product, created = Product.objects.get_or_create(
            name=product_data['name'],
            defaults=product_data
        )
        if created:
            print(f"Created product: {product_data['name']}")
            
            # Add tags to products
            if 'pajama' in product.name.lower():
                pajama_tag = Tag.objects.get(name='PAJAMA SETS')
                product.tags.add(pajama_tag)
            elif 't-shirt' in product.name.lower():
                tshirt_tag = Tag.objects.get(name='T-SHIRTS')
                product.tags.add(tshirt_tag)
            elif 'pants' in product.name.lower():
                pants_tag = Tag.objects.get(name='LOUNGE PANTS')
                product.tags.add(pants_tag)
    
    print("Dummy data created successfully!")
    print(f"Tags: {Tag.objects.count()}")
    print(f"Products: {Product.objects.count()}")
    print(f"Editorial Picks: {Product.objects.filter(is_editorial_pick=True).count()}")

if __name__ == '__main__':
    create_dummy_data()