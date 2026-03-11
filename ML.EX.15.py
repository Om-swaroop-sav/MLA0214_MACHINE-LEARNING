import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

data = load_iris()
X = data.data
y = data.target

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)

lr=LogisticRegression()
dt=DecisionTreeClassifier()
svm=SVC()

lr.fit(X_train,y_train)
dt.fit(X_train,y_train)
svm.fit(X_train,y_train)

print("Logistic Regression:",accuracy_score(y_test,lr.predict(X_test)))
print("Decision Tree:",accuracy_score(y_test,dt.predict(X_test)))
print("SVM:",accuracy_score(y_test,svm.predict(X_test)))