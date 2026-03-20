# Naive Bayes (simple)

from collections import Counter

data = [
    ['Old', 'High', 'Severe', 'Yes'],
    ['Middle', 'Medium', 'Moderate', 'Yes'],
    ['Young', 'Low', 'Mild', 'No'],
    ['Middle', 'Low', 'Mild', 'No']
]

def predict(test):
    total = len(data)
    classes = ['Yes', 'No']
    
    probs = {}
    
    for c in classes:
        subset = [row for row in data if row[-1] == c]
        prob_c = len(subset) / total
        
        for i in range(len(test)):
            count = sum(1 for row in subset if row[i] == test[i])
            prob_c *= (count + 1) / (len(subset) + 2)  # Laplace smoothing
        
        probs[c] = prob_c
    
    return probs

test = ['Middle', 'High', 'Severe']
result = predict(test)

print("Probabilities:", result)
print("Predicted Class:", max(result, key=result.get))