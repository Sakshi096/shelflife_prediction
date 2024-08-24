from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

# Load the model
model = joblib.load('models/shelf_life_model.pkl')

# Predict
y_pred = model.predict(X_test)

# Evaluate
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'MAE: {mae}')
print(f'MSE: {mse}')
print(f'R-squared: {r2}')
