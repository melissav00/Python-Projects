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

notFound= True

while first < last and notFound:
    if  answer == countries[middle]:
        notFound = False
    elif answer > countries[middle]:
        last= last-1
    elif answer < countries[middle]:
        first = first + 1

if notFound:
    print("Hello.")
else:
    print("This is on the list.")
