import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "day":[1,2,3,4,5,6,7],
    "temp":[30,32,31,29,28,27,26]
}

df = pd.DataFrame(data)
# print(df)

X = df[["day"]] # input
y = df[["temp"]] # output

#train Model
model = LinearRegression()
model.fit(X,y)

# predict temp for nect day(day 8)
prediction = model.predict([[11]])

print("Predicted temo on day 11 =",prediction[0],"Degree Celsius")