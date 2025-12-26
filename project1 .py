
import pandas as pd
import matplotlib.pyplot as plt
exam_data = {
    'Student_ID': ['S1', 'S2', 'S3', 'S4', 'S5', 'S6'],
    'Login_Count': [3, 5, 20, 4, 18, 6],
    'Tab_Switches': [1, 2, 25, 1, 22, 3],
    'Time_Spent_Minutes': [55, 50, 15, 60, 20, 48]
}

df = pd.DataFrame(exam_data)

print("Online Exam Activity Data")
print(df)
print("\nSummary Statistics")
print(df.describe())
df['Z_Login'] = (df['Login_Count'] - df['Login_Count'].mean()) / df['Login_Count'].std()
df['Z_Tab'] = (df['Tab_Switches'] - df['Tab_Switches'].mean()) / df['Tab_Switches'].std()
df['Suspicious'] = (df['Z_Login'].abs() > 2) | (df['Z_Tab'].abs() > 2)

print("\nSuspicious Activity Detection")
print(df[['Student_ID', 'Suspicious']])
plt.bar(df['Student_ID'], df['Tab_Switches'])
plt.xlabel("Student ID")
plt.ylabel("Tab Switch Count")
plt.title("Tab Switching Behavior in Online Exam")
plt.show()