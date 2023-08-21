# read from flat file
file = open("something.txt", "r")
print(file.read())

# read from csv
import csv
with open("something.csv", "r") as file:
	csv_reader = csv.reader(file)
	for line in csv_reader:
		print(line)
