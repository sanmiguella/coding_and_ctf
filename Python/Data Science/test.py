#!/usr/bin/python
import pandas as pd
import os

#data_file = "pokemon_data.txt"
data_file = "pokemon_data.csv"
#data_file = "pokemon_data.xlsx"
path = os.getcwd() + "/" + data_file
print "[+] Path -> " + path

#df = pd.read_csv(path,delimiter='\t')
df = pd.read_csv(path)
#df = pd.read_excel(path)

#print(df.columns)	# Prints header

#print(df.head(5))	# Prints first 5 rows

#print(df.tail(3))	# Prints last 3 rows

#print(df[['Name','Type 1','HP']] [0:5])	# Prints first 5 entry using the columns Name, Type 1, HP

#print(df.iloc[0:3])	# Prints row 0 to 2

#print(df.iloc[3,1])	# Print only Name from row 3 

'''
for index, row in df.iterrows():
    print(index, row['Name'])
'''
#print df.loc[df['Name'] == 'Charmander']	# Prints only the row that contains the name -> Charmander

#print df.loc[df['Type 1'] == 'Fire']		# Prints only the row where entry is 'Fire' under Column 'Type 1'

#print(df.describe())				# Prints stats like count,mean,std,min,25%,50%,75%,max

'''
name_sorted = df.sort_values('Name')		# Sorts data in ascending alphabetical order(a-z)
print(name_sorted.head(5))			# Prints the first 5 of the data which has been sorted by name in ascending order
'''

'''
name_sorted_descending = df.sort_values('Name',ascending=False)	# Sorts data in descending alphabetical order(z-a)
print(name_sorted_descending.head(5))				# Prints the first 5 of the data which has been sorted by name in descending order
'''

'''
sorted_data = df.sort_values(['Type 1','HP'])	# Sort in ascending the pokemon type(a-z) as well as its HP(from lowest to highest)
print(sorted_data.head(5))			# Prints only the first 5
'''

'''
sorted_data = df.sort_values(['Type 1','HP'], ascending=True)  
print(sorted_data.head(20))
'''

'''
sorted_data = df.sort_values(['Type 1','HP'], ascending=False)  # Sort in descending order the pokemon type(z-a) as wll as its HP(from highest to lowest)
print(sorted_data.head(20)) # Prints the first 20
'''

'''
sorted_data = df.sort_values(['Type 1','HP'], ascending=[1,0])  # Sort in ascending order the pokemon type(a-z) and HP in descending order(from highest to lowest)
print(sorted_data)
'''

df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
sorted_data = df.sort_values(['Total'], ascending=False)
print(sorted_data.head(20))
