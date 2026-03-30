import pandas as pd
symptom_weights = {
    "Chest Pain": 9,
    "Fever": 3,
    "Broken Bone": 7,
    "Cough": 2,
    "Headache": 1,
    "Difficulty Breathing": 10
}

# 2. PATIENT DATA: New entries in the ER
data = {
    'Name': ['Rahul', 'Anjali', 'Vikram', 'Sneha'],
    'Symptom': ['Fever', 'Chest Pain', 'Cough', 'Difficulty Breathing'],
    'Age': [25, 60, 30, 45]
}
df = pd.DataFrame(data)
def calculate_priority(row):
    weight = symptom_weights.get(row['Symptom'],0)
    age_factor = row['Age'] / 20
    return weight + age_factor
df['Priority_Score'] = df.apply(calculate_priority,axis=1)
print("-----Emergency Room Priority List-----")
print(df[['Name','Symptom','Priority_Score']])
print(f"\nNext Patient for Doctor:{df.iloc[0]['Name']}")
