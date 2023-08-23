from operator import attrgetter, methodcaller, itemgetter

# scores = [18, 6, 21, 20, 43, 22, 33, 60, 8, 4, 3, 6, 16, 31, 34]

# sorted_scores = sorted(scores)
# print(sorted_scores)

# reverse_sorted_scores = sorted(scores, reverse=True)
# print(reverse_sorted_scores)

class Product():
    def __init__(self, name, price, weight, discount):
        self.name = name
        self.price = price
        self.weight = weight
        self.discount = discount

    def __repr__(self):
        return repr((self.name, self.price, self.weight))

    def discount_price(self):
        return self.price - (self.price * self.discount)


product_list = [
    Product("Laptop", 60, 30, 0.05),
    Product("Laptop", 60, 10, 0.05),
    Product("Phone", 100, 40, 0.1),
    Product("Router", 20, 15, 0.25),
    Product("Camera", 75, 80, 0.75),
]

# print("Attrgetter Method:")
# print(sorted(product_list, key=attrgetter("weight"), reverse=True))

# print("Methodcaller :")
# print(sorted(product_list, key=methodcaller("discount_price")))

dumbbels = [("dumbbell", 15),
            ("dumbbell", 50),
            ("dumbbell", 20),
            ("dumbbell", 5),
            ("dumbbell", 25),
            ("dumbbell", 10)
           ]

print(sorted(dumbbels, key=itemgetter(1)))

# print(sorted(product_list, key=lambda p:p.price))
# result = (sorted(product_list, key=lambda p:p.weight))
# print(sorted(result, key=lambda p:p.price))

# def sort_products(product):
#     return product.price

# print(sorted(product_list, key=sort_products))

# print(sorted(product_list, key=lambda p:p.price))

# print(sorted(product_list, key=lambda p:p.discount_price()))