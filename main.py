import csv

with open('compiegne/60159_000AW.csv', newline='') as file:
    reader = csv.reader(file, delimiter=';')
    line = 0
    for row in reader:
        if line == 1:
            print(', '.join(row))
            break
        line += line + 1
