#!/usr/bin/python
import pandas as pd
import os 

path = os.getcwd() 
data_file = "weather_data.csv" 
full_path = path + "/" + data_file

df = pd.read_csv(full_path)
rows, columns = df.shape    # Get the number of rows, columns of the data

print "Rows: " + str(rows)
print "Columns: " + str(columns) + "\n"

print df.head(2)            # Print first 2 rows

print "\n"
print df.tail(2)            # Print last 2 rows

print "\n"
print df[2:5]               # Print rows 2 to 4

print "\n"
print df[:]                 # Prints everything

print "\n"
print df.columns            # Prints only columns

print "\n"
print df.day.head(2)        # Prints only the first 2 rows of the column named "day"

print "\n"
print df.temperature.tail(2)    # Prints only the last 2 rows of the column named "temperature"

print "\n"
print df[['event','temperature']].tail(2)   # Prints only the last 2 rows of the column named "event" and "temperature"
