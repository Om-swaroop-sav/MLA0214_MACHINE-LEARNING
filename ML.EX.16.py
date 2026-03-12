import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data=pd.read_csv("mobile_price.csv")

X=data.drop("price_range",axis=1)
y=data["price_range"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)

model=DecisionTreeClassifier()
model.fit(X_train,y_train)

pred=model.predict(X_test)

print("Accuracy:",accuracy_score(y_test,pred))