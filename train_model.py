import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# Load dataset
data = pd.read_csv("house_data.csv")

# Features
X = data[["area", "bedrooms", "bathrooms", "parking"]]

# Target
y = data["price"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Linear Regression
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

linear_predictions = linear_model.predict(X_test)
linear_accuracy = r2_score(y_test, linear_predictions)

# Random Forest
random_forest = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

random_forest.fit(X_train, y_train)

rf_predictions = random_forest.predict(X_test)
rf_accuracy = r2_score(y_test, rf_predictions)

# Print results
print("Models trained successfully!")
print()
print("Linear Regression Accuracy:", linear_accuracy)
print("Random Forest Accuracy:", rf_accuracy)

# Save Random Forest model
with open("house_price_model.pkl", "wb") as file:
    pickle.dump(random_forest, file)

print()
print("Best model saved successfully!")