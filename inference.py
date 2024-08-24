import joblib
import pandas as pd

# Load the model
model = joblib.load('models/shelf_life_model.pkl')

# New data (example)
new_data = pd.DataFrame({
    'Temperature (°C)': [5],
    'Humidity (%)': [85],
    'Packaging Type': ['plastic'],
    'Initial Quality Score': [7],
    'Produce Type': ['apple']
})

# Predict
predicted_shelf_life = model.predict(new_data)
print(f'Predicted Shelf Life: {predicted_shelf_life[0]} days')
