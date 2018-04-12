# warm up
from product import Product

p = Product("Phone", 340.0, False)
p.put_on_sale(0.1)
assert p.is_on_sale, "put_on_sale is broken"

p._name = "Hi"
p._name = "Bob"
p.__price = -5
print(p.__price)
p.whatever = 67
print(p)

# x = 5
# y = '5'
# print(repr(x), repr(y))

p2 = Product()
print(p)

# p.name = "Phone"
# p.price = 340

# print(p.price)

# products = [["Phone", 340, False], ["PC", 1420.95, True], ["Plant", 24.5, True]]
products = [Product("Phone", 340, False), Product("PC", 1420.95, True), Product("Plant", 24.5, True)]
on_sale_products = [product for product in products if product.is_on_sale]
# on_sale_products[0].price ** 2
print([str(product) for product in on_sale_products])
print(on_sale_products)

s = "Hello"
