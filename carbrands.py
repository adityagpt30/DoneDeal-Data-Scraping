#Code to filter excel file for car brands


import pandas as pd
import re

# Read the XLSX file with the original data
df = pd.read_excel('/Users/Mac/Desktop/DoneDealCarsV2.xlsx')

# Define a predefined list of car brands
car_brands = [
    "Abarth", "Acura", "Alfa Romeo", "Alpine", "Aston Martin", "Audi", "Bentley", "BMW", "Bugatti",
    "Buick", "Cadillac", "Chevrolet", "Chrysler", "Citroën", "Cupra", "Dacia", "Daihatsu", "Dodge",
    "DS Automobiles", "Ferrari", "Fiat", "Ford", "Genesis", "GMC", "Honda", "Hummer", "Hyundai",
    "Infiniti", "Isuzu", "Iveco", "Jaguar", "Jeep", "Kia", "Koenigsegg", "Lamborghini", "Lancia",
    "Land Rover", "Lexus", "Lincoln", "Lotus", "Lucid Motors", "Mahindra", "Maserati", "Maybach",
    "Mazda", "McLaren", "Mercedes-Benz", "MG", "Mini", "Mitsubishi", "Morgan", "Nissan", "Opel",
    "Pagani", "Peugeot", "Polestar", "Porsche", "RAM", "Renault", "Rivian", "Rolls-Royce", "Saab",
    "SEAT", "Skoda", "Smart", "SsangYong", "Subaru", "Suzuki", "Tata Motors", "Tesla", "Toyota",
    "Vauxhall", "Volkswagen", "Volvo", "Wiesmann", "Mercedes", "VW", "Citroen", "Range Rover"
]

# Define a function to extract car brand from title
def extract_car_brand(title):
    title = title.lower()  # Convert title to lowercase for case-insensitive comparison
    
    for brand in car_brands:
        brand_lower = brand.lower()
        
        if brand_lower in title:
            return brand

        # Handle variations and spelling mistakes in car brand names
        brand_parts = re.findall(r'\b\w+\b', brand_lower)
        for part in brand_parts:
            if part in title:
                return brand
    
    return 'Other'  # If no car brand found in the title, assign 'Other'

# Apply the function to create a new 'Car Brand' column
df['CarBrand'] = df['Title'].apply(extract_car_brand)

# Save the updated dataframe back to the XLSX file
df.to_excel('DoneDealCarsV3.xlsx', index=False)

print("New column 'Car Brand' has been added to the XLSX file.")