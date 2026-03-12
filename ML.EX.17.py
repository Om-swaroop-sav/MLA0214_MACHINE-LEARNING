import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = {
    'ram':[4,6,8,2,3,12,16,6],
    'battery':[3000,3500,4000,2000,2500,5000,6000,3500],
    'camera':[12,16,20,8,10,48,64,16],
    'price_range':[1,2,3,0,1,3,3,2]
}

df = pd.DataFrame(data)

X = df[['ram','battery','camera']]
y = df['price_range']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3)

model = DecisionTreeClassifier()

model.fit(X_train,y_train)

pred = model.predict(X_test)

print("Accuracy:",accuracy_score(y_test,pred))