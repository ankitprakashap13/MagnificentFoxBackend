from django.core.management.base import BaseCommand
from api.models import Tag, Country, Product, ProductImage
import random
from decimal import Decimal

class Command(BaseCommand):
    help = 'Populate database with sample data'

    def handle(self, *args, **options):
        # Create Tags
        tags_data = [
            'NEW-ARRIVALS', 'TRENDING', 'BESTSELLER', 'PREMIUM', 'EDITORIAL', 
            'CUSTOMER-FAVORITE', 'STAFF-PICKS', 'VALUE-FOR-MONEY', 'HAS-VIDEO',
            'SUMMER-COLLECTION', 'WINTER-ESSENTIALS', 'CASUAL-WEAR', 'FORMAL-WEAR',
            'STREETWEAR', 'VINTAGE', 'LIMITED-EDITION', 'SUSTAINABLE', 'HANDCRAFTED'
        ]
        
        for tag_name in tags_data:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            if created:
                self.stdout.write(f'Created tag: {tag_name}')

        # Create Countries
        countries_data = [
            {'name': 'India', 'code': 'IN'},
            {'name': 'New Zealand', 'code': 'NZ'}
        ]
        
        for country_data in countries_data:
            country, created = Country.objects.get_or_create(
                code=country_data['code'],
                defaults={'name': country_data['name'], 'is_active': True}
            )
            if created:
                self.stdout.write(f'Created country: {country_data["name"]}')

        # Image URLs
        image_urls = [
            "https://magnificentfox.blr1.cdn.digitaloceanspaces.com/magnificentfox/7_c2820747-f4d4-4aa3-ab4c-59b343117c8a.webp",
            "https://magnificentfox.blr1.cdn.digitaloceanspaces.com/magnificentfox/WhatsApp%20Image%202025-06-29%20at%2013.11.53_5b5ceab7.jpg",
            "https://magnificentfox.blr1.cdn.digitaloceanspaces.com/magnificentfox/WhatsApp%20Image%202025-06-29%20at%2013.11.54_7a2af981.jpg",
            "https://magnificentfox.blr1.cdn.digitaloceanspaces.com/magnificentfox/WhatsApp%20Image%202025-07-07%20at%2019.16.16_64912d63.jpg",
            "https://magnificentfox.blr1.cdn.digitaloceanspaces.com/magnificentfox/WhatsApp%20Image%202025-07-10%20at%2022.07.30_40372f48.jpg",
            "https://magnificentfox.blr1.cdn.digitaloceanspaces.com/magnificentfox/trending-mobile-wallpapers-hd-wallpapers-images%20(1)%20(1).jpg",
            "https://magnificentfox.blr1.cdn.digitaloceanspaces.com/magnificentfox/trending-mobile-wallpapers-hd-wallpapers-images.jpg"
        ]

        # Create Products
        products_data = [
            {
                "name": "Sunset Orange Co-ord",
                "description": "Vibrant sunset orange co-ord set for casual wear",
                "price": "1999.00",
                "mrp": "2399.00",
                "sizes": "s,xl",
                "quantity": 6,
                "cash_on_delivery": False,
                "customer_reviews": "The color is amazing! Fits perfectly and looks great."
            },
            {
                "name": "Charcoal Grey Lounge Set",
                "description": "Comfortable charcoal grey lounge set for relaxation",
                "price": "2199.00",
                "mrp": "2599.00",
                "quantity": 16,
                "cash_on_delivery": True,
                "customer_reviews": "Perfect for weekend lounging. Very cozy and warm."
            },
            {
                "name": "Cream Silk Blend Top",
                "description": "Elegant cream colored silk blend top",
                "price": "1699.00",
                "mrp": "1999.00",
                "quantity": 13,
                "cash_on_delivery": True,
                "customer_reviews": "Feels luxurious and looks elegant. Great quality."
            },
            {
                "name": "Pink Rose Co-ord Set",
                "description": "Matching top and bottom co-ord set with rose print",
                "price": "2299.00",
                "mrp": "2799.00",
                "quantity": 9,
                "cash_on_delivery": True,
                "customer_reviews": "Beautiful set. The fit is perfect and fabric is soft."
            },
            {
                "name": "Lavender Dreams Pajama Set",
                "description": "Soft lavender colored pajama set with dreamy comfort",
                "price": "2599.00",
                "mrp": "2999.00",
                "quantity": 7,
                "cash_on_delivery": True,
                "customer_reviews": "The color is gorgeous and it's so comfortable to wear."
            },
            {
                "name": "Denim Blue Lounge Pants",
                "description": "Comfortable denim-style lounge pants",
                "price": "1799.00",
                "mrp": "2199.00",
                "quantity": 14,
                "cash_on_delivery": True,
                "customer_reviews": "Stylish and comfortable. Great for lounging at home."
            },
            {
                "name": "Summer Linen Lounge Pants",
                "description": "Breathable linen pants perfect for summer lounging",
                "price": "1599.00",
                "mrp": "1899.00",
                "quantity": 12,
                "cash_on_delivery": True,
                "customer_reviews": "Very breathable and comfortable. Perfect for hot weather."
            },
            {
                "name": "Midnight Black Silk Dress",
                "description": "Elegant midnight black silk dress for special occasions",
                "price": "3299.00",
                "mrp": "3999.00",
                "sizes": "s,m,l",
                "quantity": 8,
                "cash_on_delivery": True,
                "customer_reviews": "Absolutely stunning! Perfect for evening events."
            },
            {
                "name": "Forest Green Casual Shirt",
                "description": "Comfortable forest green casual shirt for everyday wear",
                "price": "1299.00",
                "mrp": "1599.00",
                "sizes": "m,l,xl",
                "quantity": 20,
                "cash_on_delivery": True,
                "customer_reviews": "Great quality fabric and perfect fit."
            },
            {
                "name": "Royal Blue Evening Gown",
                "description": "Stunning royal blue evening gown with intricate details",
                "price": "4599.00",
                "mrp": "5299.00",
                "sizes": "s,m,l,xl",
                "quantity": 5,
                "cash_on_delivery": False,
                "customer_reviews": "Received so many compliments! Worth every penny."
            },
            {
                "name": "Coral Pink Summer Dress",
                "description": "Light and breezy coral pink summer dress",
                "price": "1899.00",
                "mrp": "2299.00",
                "sizes": "s,m,l",
                "quantity": 15,
                "cash_on_delivery": True,
                "customer_reviews": "Perfect for summer outings. Very comfortable."
            },
            {
                "name": "Emerald Green Blouse",
                "description": "Sophisticated emerald green blouse for office wear",
                "price": "1799.00",
                "mrp": "2199.00",
                "sizes": "s,m,l,xl",
                "quantity": 18,
                "cash_on_delivery": True,
                "customer_reviews": "Professional look with great comfort."
            },
            {
                "name": "Golden Yellow Maxi Dress",
                "description": "Flowing golden yellow maxi dress for beach vacations",
                "price": "2399.00",
                "mrp": "2899.00",
                "sizes": "s,m,l",
                "quantity": 10,
                "cash_on_delivery": True,
                "customer_reviews": "Love the color and the flow of the dress."
            },
            {
                "name": "Burgundy Velvet Jacket",
                "description": "Luxurious burgundy velvet jacket for winter evenings",
                "price": "3599.00",
                "mrp": "4299.00",
                "sizes": "m,l,xl",
                "quantity": 6,
                "cash_on_delivery": False,
                "customer_reviews": "Excellent quality velvet. Very warm and stylish."
            },
            {
                "name": "Ivory Lace Top",
                "description": "Delicate ivory lace top for romantic occasions",
                "price": "1499.00",
                "mrp": "1799.00",
                "sizes": "s,m,l",
                "quantity": 22,
                "cash_on_delivery": True,
                "customer_reviews": "Beautiful lace work. Very feminine and elegant."
            },
            {
                "name": "Turquoise Bohemian Skirt",
                "description": "Flowy turquoise bohemian skirt with ethnic prints",
                "price": "1699.00",
                "mrp": "1999.00",
                "sizes": "s,m,l,xl",
                "quantity": 13,
                "cash_on_delivery": True,
                "customer_reviews": "Love the bohemian vibe. Great for festivals."
            },
            {
                "name": "Plum Purple Cardigan",
                "description": "Cozy plum purple cardigan for chilly evenings",
                "price": "2199.00",
                "mrp": "2599.00",
                "sizes": "s,m,l,xl",
                "quantity": 11,
                "cash_on_delivery": True,
                "customer_reviews": "Super soft and warm. Perfect for layering."
            },
            {
                "name": "Sage Green Palazzo Pants",
                "description": "Comfortable sage green palazzo pants for casual wear",
                "price": "1399.00",
                "mrp": "1699.00",
                "sizes": "s,m,l,xl",
                "quantity": 17,
                "cash_on_delivery": True,
                "customer_reviews": "Very comfortable and stylish. Great for daily wear."
            },
            {
                "name": "Rose Gold Sequin Top",
                "description": "Glamorous rose gold sequin top for party nights",
                "price": "2799.00",
                "mrp": "3299.00",
                "sizes": "s,m,l",
                "quantity": 9,
                "cash_on_delivery": False,
                "customer_reviews": "Perfect for parties! Gets lots of attention."
            },
            {
                "name": "Dusty Rose Midi Skirt",
                "description": "Elegant dusty rose midi skirt for office and casual wear",
                "price": "1599.00",
                "mrp": "1899.00",
                "sizes": "s,m,l,xl",
                "quantity": 14,
                "cash_on_delivery": True,
                "customer_reviews": "Versatile piece. Can dress up or down easily."
            }
        ]

        all_tags = list(Tag.objects.all())
        all_countries = list(Country.objects.all())

        for product_data in products_data:
            # Calculate discount percentage
            price = Decimal(product_data['price'])
            mrp = Decimal(product_data['mrp'])
            discount_percentage = ((mrp - price) / mrp * 100).quantize(Decimal('0.01'))

            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults={
                    'description': product_data['description'],
                    'price': price,
                    'mrp': mrp,
                    'discount_percentage': discount_percentage,
                    'inclusive_of_taxes': True,
                    'sizes': product_data.get('sizes'),
                    'quantity': product_data['quantity'],
                    'cash_on_delivery': product_data['cash_on_delivery'],
                    'customer_reviews': product_data['customer_reviews'],
                    'is_editorial_pick': random.choice([True, False])
                }
            )

            if created:
                # Add random tags (2-4 tags per product)
                random_tags = random.sample(all_tags, random.randint(2, 4))
                product.tags.set(random_tags)

                # Add random countries (1-2 countries per product)
                random_countries = random.sample(all_countries, random.randint(1, 2))
                product.countries.set(random_countries)

                # Add random images (1-3 images per product)
                num_images = random.randint(1, 3)
                selected_images = random.sample(image_urls, num_images)
                
                for img_url in selected_images:
                    ProductImage.objects.create(
                        product=product,
                        image=img_url,
                        alt_text=f"{product.name} - Product Image"
                    )

                self.stdout.write(f'Created product: {product.name}')

        self.stdout.write(self.style.SUCCESS('Successfully populated database with sample data!'))