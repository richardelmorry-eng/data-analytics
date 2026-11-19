import random

products = ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam',
            'Headset', 'Docking Station', 'USB Hub', 'Desk Lamp', 'Surge Protector']

# 4a. Product of the Day: one randomly selected item
product_of_the_day = random.choice(products)
print(f"Product of the Day: {product_of_the_day}")

# 4b. Usability survey: 3 different products (no repeats)
survey_products = random.sample(products, 3)
print(f"Usability survey products: {survey_products}")

# 4c. Presentation: shuffle all products (shuffle changes the list in place)
random.shuffle(products)
print(f"Shuffled products: {products}")

# 4d. Simulated daily transaction count between 50 and 300
transactions = random.randint(50, 300)
print(f"Daily transaction count: {transactions}")