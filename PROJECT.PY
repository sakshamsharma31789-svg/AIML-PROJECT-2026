import pandas as pd
import random

# 1. KNOWLEDGE BASE: Symptom weights (Scale 1-10)
symptom_severity = {
    "Chest Pain": 9,
    "Fever": 3,
    "Broken Bone": 7,
    "Cough": 2,
    "Difficulty Breathing": 10
}

# 2. PATIENT DATA (Syllabus: Data Representation)
data = {
    'Name': ['Rahul', 'Anjali', 'Vikram', 'Sneha', 'Amit'],
    'Symptom': ['Fever', 'Chest Pain', 'Cough', 'Difficulty Breathing', 'Broken Bone'],
    'Age': [25, 65, 30, 45, 12]
}
df = pd.DataFrame(data)

# 3. THE PROBABILISTIC AGENT (Syllabus: Probability for ML)
def calculate_priority_score(row):
    # Base severity from symptom
    base_score = symptom_severity.get(row['Symptom'], 0)
    
    # Probabilistic Risk Factor: Older age increases risk (P(Risk|Age))
    # We normalize age to a 0-1 scale
    age_risk = row['Age'] / 100 
    
    # Final Utility Function: f(n) = Severity + Risk_Factor
    return round(base_score + (age_risk * 5), 2)

# Applying the Intelligent Agent's logic
df['Priority_Score'] = df.apply(calculate_priority_score, axis=1)

# 4. ACTION: Rational Decision Making (Sorting by urgency)
df_sorted = df.sort_values(by='Priority_Score', ascending=False)

# Output
print("--- PRIORITY LIST---")
print(df_sorted[['Name', 'Symptom', 'Age', 'Priority_Score']])
print(f"\n[AI DECISION]: Immediately attend to {df_sorted.iloc[0]['Name']} first.")
