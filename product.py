'''
create a product object
name, description, brand, model, price return discount

calculate the total number of object's price

'''
                                #solution
class Product:
    def __init__(self, name, description, brand, model, price ):
        self.name = name
        self.description = description
        self.brand = brand
        self.model = model
        self.price = price

    def get_discount(self, discount_percentage):
         return self.price * discount_percentage / 100 # 100 is percentage
    
# create multiple product instances
product1 = Product(name="Laptop", description="High performance laptop", brand="BrandX", model="ModeY", price=1000)
product2 = Product(name="Smartphone", description="Latest model smartphone", brand="BrandZ", model="ModeA", price=800)
product3 = Product(name="Tablet", description="Lightweight and portable tablet", brand="BrandY", model="ModeB", price=500)

    #List of products
products = [product1, product2, product3]

    #Calculate the total price for all products
total_price = sum(product.price for product in products) # is a concise way to calculate the total price of multiple 'product' and sum is addding these price together
print(f"Total price for all products: ₦{total_price}")

#Example of caculating and princing discount for each product
for product in products:
    discount = product.get_discount(10)  # 10% discount
    print(f"Discount for {product.name}: ₦{discount}")
    
    '''
    Explaination:
1. The 'product' class is defined with attrubes for the name, description, brand, model and price.
2. The 'get_discount' method calculates the dicount amount based on the given percentage.
3. Three 'product' instances ('product1', 'product2' and 'product3') are created with different attributes.
4. The products are added to a list called 'products'.
5. The total price for all products is calculated by summing up their prices.
6. The total price is printed.
7. An example loop calculate and prints a 10% discount for each products.
8. 'sum()' is a built-in python function that takes an iterable and returns rhe saum of its elements. 
    '''

