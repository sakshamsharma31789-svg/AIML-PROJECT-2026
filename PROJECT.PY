import pandas as pd
import random
#Assigning weights to the symptoms of the patient
s = {
    "Chest Pain": 9,"Fever": 3,"Broken Bone": 7,"Cough": 2,"Difficulty Breathing": 10
}
#Data of the patient in the hospital used
data = {
'Name': ['Rahul', 'Anjali', 'Vikram', 'Sneha', 'Amit'],
 'Symptom': ['Fever', 'Chest Pain', 'Cough', 'Difficulty Breathing', 'Broken Bone'],
'Age': [25, 65, 30, 45, 12]
}
df = pd.DataFrame(data)

#Using probability for the decision making for the priority
def score(row):
 x = s.get(row['Symptom'], 0)
    
    
 age_risk = row['Age'] / 100 
    
 return round(x + (age_risk * 5), 2)

# Applying the probability logic above and assigning it to priority row
df['Priority'] = df.apply(score, axis=1)

#Sorting the scores of patient in descending order
df_sorted = df.sort_values(by='Priority', ascending=False)

#Output the priority list
print("--- PRIORITY LIST---")
print(df_sorted[['Name', 'Symptom', 'Age', 'Priority']])
print(f"\n[AI DECISION]: Immediately attend to {df_sorted.iloc[0]['Name']} first.")
