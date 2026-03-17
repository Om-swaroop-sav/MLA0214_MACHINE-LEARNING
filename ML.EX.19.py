import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

data = pd.DataFrame({
    'Income':[5000,6000,2500,7000,3000,8000,4000,10000],
    'Credit':[600,650,500,700,550,750,580,800],
    'Loan_Status':[1,1,0,1,0,1,0,1]
})

X = data[['Income','Credit']]
y = data['Loan_Status']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = GaussianNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(accuracy_score(y_test, y_pred))