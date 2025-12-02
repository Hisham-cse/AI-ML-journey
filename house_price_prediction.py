import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
# dataset
data = {
    "size_sqft": [1400, 1600, 1700, 1875, 1100, 1550, 1800, 2400],
    "bedrooms":  [3, 3, 3, 4, 2, 3, 4, 4],
    "price":     [245000, 312000, 279000, 308000, 199000, 310000, 360000, 410000]
}
df = pd.DataFrame(data)
X = df[["size_sqft","bedrooms"]] #features
y = df["price"]                  #labels
# Train-test split
X_train , X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state = 42)
# Build model
model = LinearRegression()
model.fit(X_train,y_train)
# Predictions
y_pred = model.predict(X_test)
# Metrics
mae = mean_absolute_error(y_test,y_pred)
mse = mean_squared_error(y_test,y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test,y_pred)
print("Predicted Prices",y_pred)
print("MAE:",mae)
print("RMSE:",rmse)
print("R2 Score:",r2)

# predict for new house
new_house = [[1800,3]]  #1800 sqft, 3 bedrooms
predicted_price = model.predict(new_house)
print("\nPredicted price for 1800 sqft, 3BHK:",predicted_price[0])