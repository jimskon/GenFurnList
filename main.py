import random

# Define furniture names for variety
sofa_names = ["Luxury", "Comfy", "Modular", "Classic", "Modern"]
table_names = ["Dining", "Coffee", "Study", "Patio", "Glass"]
chair_names = ["Office", "Gaming", "Dining", "Recliner", "Folding"]

# Function to generate random values for quantity, price, and specific attributes
def generate_random_furniture():
    furniture_list = []
    
    for _ in range(100):
        furniture_type = random.choice(["sofa", "table", "chair"])
        name = ""
        quantity = random.randint(1, 10)
        price = round(random.uniform(50, 1000), 2)
        
        if furniture_type == "sofa":
            name = random.choice(sofa_names)
            num_seats = random.randint(2, 5)
            furniture_list.append(f"{furniture_type},{name},{quantity},{price},{num_seats}")
        
        elif furniture_type == "table":
            name = random.choice(table_names)
            num_legs = random.randint(3, 6)
            furniture_list.append(f"{furniture_type},{name},{quantity},{price},{num_legs}")
        
        elif furniture_type == "chair":
            name = random.choice(chair_names)
            has_armrests = random.choice([True, False])
            furniture_list.append(f"{furniture_type},{name},{quantity},{price},{has_armrests}")
    
    return furniture_list

# Generate the random furniture data
random_furniture_data = generate_random_furniture()

# Output the data
random_furniture_data[:10]  # Display first 10 rows as a sample
