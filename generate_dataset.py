import pandas as pd
import random

data = []

for i in range(1000):

    area = random.randint(500, 4000)
    bedrooms = random.randint(1, 5)
    bathrooms = random.randint(1, 4)
    parking = random.randint(0, 3)

    # Synthetic price formula for project/demo purposes
    price = (
        area * 3000
        + bedrooms * 250000
        + bathrooms * 150000
        + parking * 100000
    )

    # Small variation
    price += random.randint(-200000, 200000)

    data.append([
        area,
        bedrooms,
        bathrooms,
        parking,
        price
    ])

df = pd.DataFrame(
    data,
    columns=[
        "area",
        "bedrooms",
        "bathrooms",
        "parking",
        "price"
    ]
)

df.to_csv("house_data.csv", index=False)

print("1000 house records created successfully!")
print("Dataset saved as house_data.csv")