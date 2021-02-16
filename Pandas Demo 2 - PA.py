# Created by Peter Anastasopoulos

# Importing the pandas library which will be used
import pandas as pd

# Reading in the data file
df = pd.read_csv("survey_data.csv")

# Part 1 - Table of Communication domain category

# Dropping all missing values in the communication category
CG_no_null = df['COMGENCategory'].dropna()

# Creating variables that will be used to count our frequencies
vul = 0
at_risk = 0
on_track = 0

# Looping through all values and placing in their categories, using survey_data_map for categories
for elem in CG_no_null:
    if elem == 1:
        vul += 1
    if elem == 2:
        at_risk += 1
    if elem == 3 or elem == 4:
        on_track += 1

# Converting the frequencies as a percentage
CG_total = CG_no_null.count()
vul_pct = round((vul / CG_total) * 100, 2)
at_risk_pct = round((at_risk / CG_total) * 100, 2)
on_track_pct = round((on_track / CG_total) * 100, 2)

# Creating a data variable with all the information collected along with column names
data_1 = {'Category': ['Vulnerable', 'At risk', 'On track'],
          'Frequency': [vul, at_risk, on_track],
          'Percentage': [vul_pct, at_risk_pct, on_track_pct]}

# Creating another pandas dataframe, to display the results as a table
results_df1 = pd.DataFrame(data_1, columns=['Category', 'Frequency', 'Percentage'])

# Printing the resulting table
print('Table 1')
print(results_df1)

# Part 2 - Statistics of the language and cognition domain category

# Dropping all missing values in the language and cognition category
df['LANGCOGCategory'].dropna()

# Dropping all records that aren't on track
df = df.drop(df[df.LANGCOGCategory == 1].index)
df = df.drop(df[df.LANGCOGCategory == 2].index)

# Printing the frequency table
df2 = pd.value_counts(df.Region).to_frame().reset_index()
print(df2)
