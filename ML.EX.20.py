import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

data = pd.DataFrame({
    'TV':[100,200,300,400,150,250,350,450],
    'Radio':[10,20,30,40,15,25,35,45],
    'Newspaper':[5,10,15,20,7,12,17,22],
    'sales':[20,40,60,80,30,50,70,90]
})

X = data[['TV','Radio','Newspaper']]
y = data['sales']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(mean_absolute_error(y_test, y_pred))