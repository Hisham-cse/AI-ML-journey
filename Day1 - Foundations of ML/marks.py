from sklearn.linear_model import LinearRegression
hours = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
marks = [40,46,50,60,80,40,46,50,60,80]

model = LinearRegression()
model.fit(hours,marks)

print("Marks of 6 hours",model.predict([[6]])[0])
print("Marks of 9 hours",model.predict([[9]])[0])