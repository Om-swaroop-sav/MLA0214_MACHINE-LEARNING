import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "year":[2015,2016,2017,2018,2019],
    "km_driven":[50000,40000,30000,20000,10000],
    "price":[500000,600000,700000,800000,900000]
}

df = pd.DataFrame(data)

X = df[['year','km_driven']]
y = df['price']

model = LinearRegression()
model.fit(X,y)

pred = model.predict([[2020,15000]])

print("Predicted Car Price:",pred)