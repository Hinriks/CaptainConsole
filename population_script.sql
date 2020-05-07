INSERT INTO manufacturer_manufacturer (name, logo, year_of_start) VALUES('Playstation', 'https://ceowatermandate.org/wp-content/uploads/2017/08/nestle-company-vector-logo-400x400.png', '01-01-1866');
INSERT INTO manufacturer_manufacturer (name, logo, year_of_start) VALUES('Nintendo', 'http://www.logospng.com/images/182/logo-haribo-182083.png', '12-13-1920');

INSERT INTO product_candycategory (name) VALUES('Playstation');
INSERT INTO product_candycategory (name) VALUES('Nintendo');


INSERT INTO product_product (name, description, price, on_sale, category_id, manufacturer_id) VALUES('Playstation 3', 'First launched in the UK in 1935 it has become an iconic snack bar ever since. Just unwrap the bar, break off one of the fingers and savour the deliciously smooth milk chocolate.', 49995, false, 1, 1);
INSERT INTO product_product (name, description, price, on_sale, category_id, manufacturer_id) VALUES('Xbox One', 'Delicous Hershey’s Milk Chocolate with crunchy little cookie pieces', 1.99, true, 2, 2);

INSERT INTO product_productimage (image, product_id) VALUES('http://www.nestle-family.com/uploads/product/615f12a8d73e42f395addd1e68af9bdc.png', 1);
INSERT INTO product_productimage (image, product_id) VALUES('https://www.kitkat.com/images/kitkat-snap.png', 1);