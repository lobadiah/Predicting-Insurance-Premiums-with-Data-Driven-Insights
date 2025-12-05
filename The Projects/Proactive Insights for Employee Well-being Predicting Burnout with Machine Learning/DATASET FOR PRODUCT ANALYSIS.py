import pandas as pd
import numpy as np

# Create sample product dataset
np.random.seed(42)

data = {
    'product_id': range(1, 21),
    'product_name': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones',
                     'USB Cable', 'Desk', 'Chair', 'Webcam', 'Microphone',
                     'Speaker', 'External SSD', 'Tablet', 'Phone', 'Charger',
                     'Screen Protector', 'Phone Case', 'USB Hub', 'HDMI Cable', 'Stand'],
    'category': ['Electronics', 'Accessories', 'Accessories', 'Electronics', 'Audio',
                 'Cables', 'Furniture', 'Furniture', 'Electronics', 'Audio',
                 'Audio', 'Storage', 'Electronics', 'Electronics', 'Accessories',
                 'Accessories', 'Accessories', 'Cables', 'Cables', 'Accessories'],
    'price': np.random.randint(10, 1500, 20),
    'quantity_sold': np.random.randint(5, 500, 20),
    'rating': np.round(np.random.uniform(3.5, 5.0, 20), 1)
}

df = pd.DataFrame(data)
print(df)