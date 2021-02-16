# Created by Peter Anastasopoulos

# Reading in the pandas library which will be used
import pandas as pd

# Reading in Files
file1 = pd.read_csv('data_wrangling_medical_2020_u7183445.csv')
file2 = pd.read_csv('data_wrangling_education_2020_u7183445.csv')

# Writing the merged file
file3 = file1.merge(file2, how='inner', on='ssn', suffixes=('_medical', '_education'))
del file3["rec_id_medical"]
del file3["rec_id_education"]
file3 = file3.drop_duplicates()

# 2d - Eliminating all non-matching names
file3["exists1"] = file3.drop('first_name_medical', 1).isin(file3['first_name_medical']).any(1)
file3["exists2"] = file3.drop('middle_name_medical', 1).isin(file3['middle_name_medical']).any(1)
file3["exists3"] = file3.drop('last_name_medical', 1).isin(file3['last_name_medical']).any(1)
file3["exists5"] = file3.drop('birth_date_medical', 1).isin(file3['birth_date_medical']).any(1)

file3.drop(file3[file3["exists1"] == False].index, inplace=True)
file3.drop(file3[file3["exists2"] == False].index, inplace=True)
file3.drop(file3[file3["exists3"] == False].index, inplace=True)
file3.drop(file3[file3["exists5"] == False].index, inplace=True)

del file3["exists1"]
del file3["exists2"]
del file3["exists3"]
del file3['exists5']
del file3["first_name_education"]
del file3["middle_name_education"]
del file3["last_name_education"]
del file3["birth_date_education"]
file3.rename(columns={"first_name_medical": "first_name", "middle_name_medical": "middle_name",
                      "last_name_medical": "last_name", "birth_date_medical": "birth_date"})

# 3b
# Columns with most missing values are phone_medical (5426) and email_medical (4040)
# Replacing null values in medical with those from education
file3['phone_medical'].fillna(file3['phone_education'], inplace=True)
file3['email_medical'].fillna(file3['email_education'], inplace=True)

# 3c - Negative salary values
file3['salary'][file3['salary'] < 0] = np.nan

# 3c - Negative weight values
file3['weight'][file3['weight'] < 0] = round(file3['bmi'] * ((file3['height']/100) ** 2), 0)

# 3d - Check DOB and age
list1 = list()
for elem in file3['birth_date_medical']:
    list1.append(2020 - int(elem[-4:]))
file3['current_age'] = list1

# 4a - Timeliness

ts_list = list()
for elem in file3['employment_timestamp']:
    if 2020 - int(elem[0:4]) > 3:
        ts_list.append(elem)
file3 = file3[~file3['employment_timestamp'].isin(ts_list)]

# 4b - additional changes
# Deleting irrelevant columns
del file3['bmi']
del file3['credit_card_number']

#Format changes
file3['state_education'] = file3['state_education'].str.lower()
file3['occupation'][file3['occupation'] == 're-tired'] = 'retired'

file3['smoking_status'][file3['smoking_status'] == 1] = 'yes'
file3['smoking_status'][file3['smoking_status'] == 0] = 'no'

# Writing the csv
file3_csv = file3.to_csv('data_wrangling_merged_2020_u7183445.csv', index=False)
print(len(file3.columns))
print(len(file3))
