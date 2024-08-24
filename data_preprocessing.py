import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Load data
df = pd.read_csv('data/raw/produce_shelf_life.csv')

# Drop missing values
df = df.dropna()

# Define features and target
X = df.drop('Remaining Shelf Life (days)', axis=1)
y = df['Remaining Shelf Life (days)']

# Encode categorical variables
categorical_features = ['Packaging Type', 'Produce Type']
numerical_features = ['Temperature (°C)', 'Humidity (%)', 'Initial Quality Score']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_features),
        ('cat', OneHotEncoder(), categorical_features)])

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
