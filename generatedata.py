import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate random data
n_samples = 500

temperature = np.random.uniform(0, 20, n_samples)  # Temperature between 0°C and 20°C
humidity = np.random.uniform(50, 100, n_samples)   # Humidity between 50% and 100%
packaging = np.random.choice(['plastic', 'paper', 'none'], n_samples)
initial_quality = np.random.randint(1, 11, n_samples)  # Initial quality score between 1 and 10
produce_type = np.random.choice(['apple', 'banana', 'carrot', 'lettuce'], n_samples)

# Simple function to determine shelf life
def calculate_shelf_life(temp, humidity, packaging, quality, produce):
    base_life = 20 - temp - (humidity / 10) + quality
    if packaging == 'plastic':
        base_life += 2
    elif packaging == 'paper':
        base_life += 1
    
    # Adjust based on produce type
    if produce == 'banana':
        base_life -= 3
    elif produce == 'carrot':
        base_life += 1
    elif produce == 'lettuce':
        base_life -= 2
    
    return max(1, int(base_life))  # Shelf life should be at least 1 day

# Calculate shelf life
shelf_life = [
    calculate_shelf_life(temp, hum, pack, qual, prod)
    for temp, hum, pack, qual, prod in zip(temperature, humidity, packaging, initial_quality, produce_type)
]

# Create a DataFrame
df = pd.DataFrame({
    'Temperature (°C)': temperature,
    'Humidity (%)': humidity,
    'Packaging Type': packaging,
    'Initial Quality Score': initial_quality,
    'Produce Type': produce_type,
    'Remaining Shelf Life (days)': shelf_life
})

# Save to CSV
df.to_csv('produce_shelf_life.csv', index=False)

print("Dataset generated and saved as 'produce_shelf_life.csv'")
