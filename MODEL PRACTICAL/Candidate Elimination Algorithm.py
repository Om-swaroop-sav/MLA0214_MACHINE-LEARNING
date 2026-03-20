# Candidate Elimination Algorithm

data = [
    ['Old', 'High', 'Severe', 'Yes'],
    ['Middle', 'Medium', 'Moderate', 'Yes'],
    ['Young', 'Low', 'Mild', 'No'],
    ['Middle', 'Low', 'Mild', 'No']
]

S = ['Ø', 'Ø', 'Ø']
G = [['?', '?', '?']]

for row in data:
    if row[-1] == 'Yes':
        for i in range(len(S)):
            if S[i] == 'Ø':
                S[i] = row[i]
            elif S[i] != row[i]:
                S[i] = '?'
    else:
        for i in range(len(S)):
            if S[i] != row[i]:
                G.append(S.copy())

print("Specific Boundary S:", S)
print("General Boundary G:", G)