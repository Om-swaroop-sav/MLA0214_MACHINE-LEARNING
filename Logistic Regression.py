# Logistic Regression

from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression

data = [
    ['Old', 'High', 'Severe', 'Yes'],
    ['Middle', 'Medium', 'Moderate', 'Yes'],
    ['Young', 'Low', 'Mild', 'No'],
    ['Middle', 'Low', 'Mild', 'No']
]

X = [row[:-1] for row in data]
y = [row[-1] for row in data]

# Encoding
encoders = []
X_encoded = []

for col in range(len(X[0])):
    le = LabelEncoder()
    col_data = [row[col] for row in X]
    encoded = le.fit_transform(col_data)
    X_encoded.append(encoded)
    encoders.append(le)

X_encoded = list(zip(*X_encoded))

y_le = LabelEncoder()
y_encoded = y_le.fit_transform(y)

# Model
model = LogisticRegression()
model.fit(X_encoded, y_encoded)

# Test
test = ['Middle', 'High', 'Severe']

test_encoded = []
for i in range(len(test)):
    test_encoded.append(encoders[i].transform([test[i]])[0])

prediction = model.predict([test_encoded])
prob = model.predict_proba([test_encoded])

print("Predicted Class:", y_le.inverse_transform(prediction))
print("Probability:", prob)