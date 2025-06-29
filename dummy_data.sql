USE testDb;

-- Clean all tables first
SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE api_product_tags;
TRUNCATE TABLE api_product_offers;
TRUNCATE TABLE api_product_images;
TRUNCATE TABLE api_product_videos;
TRUNCATE TABLE api_editorialpick;
TRUNCATE TABLE api_wishlistitem;
TRUNCATE TABLE api_cartitem;
TRUNCATE TABLE api_orderitem;
TRUNCATE TABLE api_productimage;
TRUNCATE TABLE api_productvideo;
TRUNCATE TABLE api_wishlist;
TRUNCATE TABLE api_cart;
TRUNCATE TABLE api_order;
TRUNCATE TABLE api_product;
TRUNCATE TABLE api_offer;
TRUNCATE TABLE api_tag;
TRUNCATE TABLE api_user;
SET FOREIGN_KEY_CHECKS = 1;

-- Insert Tags (10 tags)
INSERT IGNORE INTO api_tag (name) VALUES 
('PAJAMA SETS'),
('SHORT SETS'),
('BOTTOMS'),
('T-SHIRTS'),
('LINEN TOPS'),
('LOUNGE PANTS'),
('CO-ORD SETS'),
('NIGHTWEAR'),
('CASUAL WEAR'),
('SUMMER COLLECTION');

-- Insert Users (10 users)
INSERT IGNORE INTO api_user (username, first_name, last_name, email, name, mobile, password, is_staff, is_active, date_joined) VALUES 
('user1', 'John', 'Doe', 'john@example.com', 'John Doe', '9876543210', 'pbkdf2_sha256$600000$test', 0, 1, NOW()),
('user2', 'Jane', 'Smith', 'jane@example.com', 'Jane Smith', '9876543211', 'pbkdf2_sha256$600000$test', 0, 1, NOW()),
('user3', 'Mike', 'Johnson', 'mike@example.com', 'Mike Johnson', '9876543212', 'pbkdf2_sha256$600000$test', 0, 1, NOW()),
('user4', 'Sarah', 'Wilson', 'sarah@example.com', 'Sarah Wilson', '9876543213', 'pbkdf2_sha256$600000$test', 0, 1, NOW()),
('user5', 'David', 'Brown', 'david@example.com', 'David Brown', '9876543214', 'pbkdf2_sha256$600000$test', 0, 1, NOW()),
('user6', 'Lisa', 'Davis', 'lisa@example.com', 'Lisa Davis', '9876543215', 'pbkdf2_sha256$600000$test', 0, 1, NOW()),
('user7', 'Tom', 'Miller', 'tom@example.com', 'Tom Miller', '9876543216', 'pbkdf2_sha256$600000$test', 0, 1, NOW()),
('user8', 'Amy', 'Garcia', 'amy@example.com', 'Amy Garcia', '9876543217', 'pbkdf2_sha256$600000$test', 0, 1, NOW()),
('user9', 'Chris', 'Martinez', 'chris@example.com', 'Chris Martinez', '9876543218', 'pbkdf2_sha256$600000$test', 0, 1, NOW()),
('user10', 'Emma', 'Lopez', 'emma@example.com', 'Emma Lopez', '9876543219', 'pbkdf2_sha256$600000$test', 0, 1, NOW());

-- Insert Products (15 products)
INSERT IGNORE INTO api_product (name, description, price, mrp, discount_percentage, inclusive_of_taxes, quantity, cash_on_delivery, customer_reviews, is_editorial_pick, created_at, updated_at) VALUES 
('Coral Rose Lucy Butter-Soft Cotton Knit Women''s Pajama Set', 'Comfortable and stylish pajama set made from butter-soft cotton', 2799.00, 2999.00, 6.67, 1, 10, 1, 'Amazing quality and super comfortable. Perfect fit!', 1, NOW(), NOW()),
('Ivy Blue Floral Cotton Blend Women''s Pajama Set', 'Beautiful floral pattern pajama set in cotton blend fabric', 2999.00, 3200.00, 6.28, 1, 8, 1, 'Love the floral design. Very comfortable for sleeping.', 1, NOW(), NOW()),
('Classic White Cotton T-Shirt', 'Basic white cotton t-shirt for everyday wear', 899.00, 1199.00, 25.02, 1, 15, 1, 'Great quality cotton. Fits perfectly and washes well.', 0, NOW(), NOW()),
('Summer Linen Lounge Pants', 'Breathable linen pants perfect for summer lounging', 1599.00, 1899.00, 15.80, 1, 12, 1, 'Very breathable and comfortable. Perfect for hot weather.', 1, NOW(), NOW()),
('Midnight Black Silk Pajama Set', 'Luxurious silk pajama set for ultimate comfort', 3499.00, 3999.00, 12.50, 1, 5, 1, 'Feels like sleeping on clouds. Absolutely love it!', 1, NOW(), NOW()),
('Striped Cotton Short Set', 'Casual striped cotton shorts and top set', 1299.00, 1599.00, 18.76, 1, 20, 1, 'Perfect for summer. Light and airy fabric.', 0, NOW(), NOW()),
('Floral Print Linen Top', 'Beautiful floral print linen top for casual wear', 1199.00, 1499.00, 20.01, 1, 18, 1, 'Love the print and the fabric quality is excellent.', 1, NOW(), NOW()),
('Denim Blue Lounge Pants', 'Comfortable denim-style lounge pants', 1799.00, 2199.00, 18.19, 1, 14, 1, 'Stylish and comfortable. Great for lounging at home.', 0, NOW(), NOW()),
('Pink Rose Co-ord Set', 'Matching top and bottom co-ord set with rose print', 2299.00, 2799.00, 17.86, 1, 9, 1, 'Beautiful set. The fit is perfect and fabric is soft.', 1, NOW(), NOW()),
('Navy Blue Cotton Nightwear', 'Classic navy blue cotton nightwear set', 1899.00, 2299.00, 17.40, 1, 11, 1, 'Simple and elegant. Very comfortable for sleeping.', 0, NOW(), NOW()),
('Lavender Dreams Pajama Set', 'Soft lavender colored pajama set with dreamy comfort', 2599.00, 2999.00, 13.34, 1, 7, 1, 'The color is gorgeous and it''s so comfortable to wear.', 1, NOW(), NOW()),
('Green Leaf Print Shorts', 'Trendy green leaf print shorts for summer', 999.00, 1299.00, 23.09, 1, 25, 1, 'Love the print! Perfect for hot summer days.', 0, NOW(), NOW()),
('Cream Silk Blend Top', 'Elegant cream colored silk blend top', 1699.00, 1999.00, 15.01, 1, 13, 1, 'Feels luxurious and looks elegant. Great quality.', 1, NOW(), NOW()),
('Charcoal Grey Lounge Set', 'Comfortable charcoal grey lounge set for relaxation', 2199.00, 2599.00, 15.39, 1, 16, 1, 'Perfect for weekend lounging. Very cozy and warm.', 0, NOW(), NOW()),
('Sunset Orange Co-ord', 'Vibrant sunset orange co-ord set for casual wear', 1999.00, 2399.00, 16.67, 1, 6, 1, 'The color is amazing! Fits perfectly and looks great.', 1, NOW(), NOW());

-- Insert Offers (10 offers)
INSERT IGNORE INTO api_offer (name, discount_percentage, start_date, end_date) VALUES 
('Summer Sale', 25.00, '2024-06-01 00:00:00', '2024-08-31 23:59:59'),
('New Year Special', 30.00, '2024-01-01 00:00:00', '2024-01-31 23:59:59'),
('Festive Discount', 20.00, '2024-10-01 00:00:00', '2024-11-30 23:59:59'),
('Flash Sale', 40.00, '2024-07-15 00:00:00', '2024-07-17 23:59:59'),
('Weekend Deal', 15.00, '2024-06-29 00:00:00', '2024-06-30 23:59:59'),
('Monsoon Offer', 35.00, '2024-07-01 00:00:00', '2024-09-30 23:59:59'),
('Back to School', 22.00, '2024-08-01 00:00:00', '2024-08-31 23:59:59'),
('Holiday Special', 28.00, '2024-12-01 00:00:00', '2024-12-31 23:59:59'),
('Spring Collection', 18.00, '2024-03-01 00:00:00', '2024-05-31 23:59:59'),
('Clearance Sale', 50.00, '2024-12-26 00:00:00', '2024-12-31 23:59:59');

-- Insert Orders (10 orders)
INSERT INTO api_order (user_id, total_price, status, created_at, updated_at) VALUES 
(1, 2799.00, 'Delivered', NOW(), NOW()),
(2, 4298.00, 'Shipped', NOW(), NOW()),
(3, 1599.00, 'Processing', NOW(), NOW()),
(4, 3499.00, 'Delivered', NOW(), NOW()),
(5, 2598.00, 'Cancelled', NOW(), NOW()),
(6, 1899.00, 'Delivered', NOW(), NOW()),
(7, 4598.00, 'Shipped', NOW(), NOW()),
(8, 1999.00, 'Processing', NOW(), NOW()),
(9, 2199.00, 'Delivered', NOW(), NOW()),
(10, 3298.00, 'Pending', NOW(), NOW());

-- Insert Order Items (15 order items)
INSERT INTO api_orderitem (order_id, product_id, quantity, price) VALUES 
(1, 1, 1, 2799.00),
(2, 1, 1, 2799.00), (2, 4, 1, 1599.00),
(3, 4, 1, 1599.00),
(4, 5, 1, 3499.00),
(5, 6, 2, 1299.00),
(6, 10, 1, 1899.00),
(7, 5, 1, 3499.00), (7, 7, 1, 1199.00),
(8, 9, 1, 1999.00),
(9, 14, 1, 2199.00),
(10, 2, 1, 2999.00);

-- Insert Carts (10 carts)
INSERT INTO api_cart (user_id, created_at, updated_at) VALUES 
(1, NOW(), NOW()),
(2, NOW(), NOW()),
(3, NOW(), NOW()),
(4, NOW(), NOW()),
(5, NOW(), NOW()),
(6, NOW(), NOW()),
(7, NOW(), NOW()),
(8, NOW(), NOW()),
(9, NOW(), NOW()),
(10, NOW(), NOW());

-- Insert Cart Items (15 cart items)
INSERT INTO api_cartitem (cart_id, product_id, quantity) VALUES 
(1, 3, 2),
(1, 7, 1),
(2, 1, 1),
(3, 4, 1),
(3, 6, 2),
(4, 5, 1),
(5, 8, 1),
(6, 9, 1),
(6, 11, 1),
(7, 12, 3),
(8, 13, 1),
(9, 14, 1),
(9, 15, 1),
(10, 2, 1),
(10, 10, 2);

-- Insert Wishlists (10 wishlists)
INSERT INTO api_wishlist (user_id, created_at, updated_at) VALUES 
(1, NOW(), NOW()),
(2, NOW(), NOW()),
(3, NOW(), NOW()),
(4, NOW(), NOW()),
(5, NOW(), NOW()),
(6, NOW(), NOW()),
(7, NOW(), NOW()),
(8, NOW(), NOW()),
(9, NOW(), NOW()),
(10, NOW(), NOW());

-- Insert Wishlist Items (12 wishlist items)
INSERT INTO api_wishlistitem (wishlist_id, product_id) VALUES 
(1, 1), (1, 5),
(2, 2), (2, 7),
(3, 3), (3, 9),
(4, 4), (4, 11),
(5, 6), (5, 13),
(6, 8), (6, 15),
(7, 10),
(8, 12),
(9, 14),
(10, 1);

-- Insert Product Images (15 product images)
INSERT INTO api_productimage (product_id, image) VALUES 
(1, 'product_images/pajama1.jpg'),
(2, 'product_images/pajama2.jpg'),
(3, 'product_images/tshirt1.jpg'),
(4, 'product_images/pants1.jpg'),
(5, 'product_images/silk_pajama.jpg'),
(6, 'product_images/shorts1.jpg'),
(7, 'product_images/linen_top.jpg'),
(8, 'product_images/lounge_pants.jpg'),
(9, 'product_images/coord1.jpg'),
(10, 'product_images/nightwear1.jpg'),
(11, 'product_images/lavender_pajama.jpg'),
(12, 'product_images/green_shorts.jpg'),
(13, 'product_images/silk_top.jpg'),
(14, 'product_images/grey_lounge.jpg'),
(15, 'product_images/orange_coord.jpg');

-- Insert Product Videos (10 product videos)
INSERT INTO api_productvideo (product_id, video) VALUES 
(1, 'product_videos/pajama1_demo.mp4'),
(2, 'product_videos/pajama2_demo.mp4'),
(5, 'product_videos/silk_pajama_demo.mp4'),
(7, 'product_videos/linen_top_demo.mp4'),
(9, 'product_videos/coord1_demo.mp4'),
(11, 'product_videos/lavender_demo.mp4'),
(13, 'product_videos/silk_top_demo.mp4'),
(15, 'product_videos/orange_coord_demo.mp4'),
(4, 'product_videos/pants_demo.mp4'),
(14, 'product_videos/grey_lounge_demo.mp4');

-- Link Products to Tags
INSERT INTO api_product_tags (product_id, tag_id) VALUES 
(1, 1), (1, 8), -- Pajama Set 1
(2, 1), (2, 8), -- Pajama Set 2
(3, 4), (3, 9), -- T-Shirt
(4, 6), (4, 10), -- Lounge Pants
(5, 1), (5, 8), -- Silk Pajama
(6, 2), (6, 10), -- Short Set
(7, 5), (7, 9), -- Linen Top
(8, 3), (8, 9), -- Denim Pants
(9, 7), (9, 9), -- Co-ord Set
(10, 8), (10, 9), -- Nightwear
(11, 1), (11, 8), -- Lavender Pajama
(12, 2), (12, 10), -- Green Shorts
(13, 5), (13, 9), -- Silk Top
(14, 6), (14, 9), -- Grey Lounge
(15, 7), (15, 9); -- Orange Co-ord

-- Link Products to Offers
INSERT INTO api_product_offers (product_id, offer_id) VALUES 
(1, 1), (2, 1), (3, 1), -- Summer Sale
(4, 2), (5, 2), -- New Year Special
(6, 3), (7, 3), (8, 3), -- Festive Discount
(9, 4), (10, 4), -- Flash Sale
(11, 6), (12, 6), (13, 6), -- Monsoon Offer
(14, 8), (15, 8); -- Holiday Special

-- Link Product Images to Products
INSERT INTO api_product_images (product_id, productimage_id) VALUES 
(1, 1), (2, 2), (3, 3), (4, 4), (5, 5),
(6, 6), (7, 7), (8, 8), (9, 9), (10, 10),
(11, 11), (12, 12), (13, 13), (14, 14), (15, 15);

-- Link Product Videos to Products
INSERT INTO api_product_videos (product_id, productvideo_id) VALUES 
(1, 1), (2, 2), (5, 3), (7, 4), (9, 5),
(11, 6), (13, 7), (15, 8), (4, 9), (14, 10);

-- Insert Editorial Picks (for products marked as editorial picks)
INSERT INTO api_editorialpick (product_id, is_active, created_at) VALUES 
(1, 1, NOW()),
(2, 1, NOW()),
(4, 1, NOW()),
(5, 1, NOW()),
(7, 1, NOW()),
(9, 1, NOW()),
(11, 1, NOW()),
(13, 1, NOW()),
(15, 1, NOW());