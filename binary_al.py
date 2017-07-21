import csv
import string

# Open the CSV File and read it in.
f = open('Countries.csv')
data = f.read()

# Split the data into an array of countries.
countries = data.split('\n')

length = len(countries)
print(countries)

# Start your search algorithm here.
first = 0
last = len(countries)
middle = int((first + last)/2)


answer = input("What country would you like?")
while first < last:
    if  answer == countries[middle]:
        print("This is the middle of the list.")
    elif answer > countries[middle]:
        print("This is in the first section of the list.")
    elif answer < countries[middle]:
        print("This is in the last section of the list.")
    else:
        print("This is not on the list.")
