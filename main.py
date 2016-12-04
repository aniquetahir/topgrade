import csv

def getFloatVal(string_val):
    if string_val == "":
        return 0.0
    else:
        return float(string_val)

with open('Recitations.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        pin = row[0]
        grades = row[1:]
        # Convert to floats
        grades = map(getFloatVal, grades)
        grades.sort(reverse=True)
        top_grades = grades[0:10]
        print '%s,%f' % (pin, sum(top_grades))
