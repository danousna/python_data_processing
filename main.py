from csv import excel, DictReader
from os import listdir
from os.path import isfile, join
from sys import stderr

dial = excel
dial.delimiter = ';'

def read_file_gen(file_name):
    with open(file_name) as f:
        reader = DictReader(f, dialect=dial)
        for r in reader:
            yield dict(r)

files = [f for f in listdir('compiegne/') if isfile(join('compiegne/', f))]
count = 0
parcelles = {}

for file_name in files:
    gen = read_file_gen(join('compiegne/', file_name))
    for item in gen:
        count = count + 1
        if item['Code parcelle'] in parcelles.keys():
            parcelles[item['Code parcelle']] = parcelles[item['Code parcelle']] + 1
        else:
            parcelles[item['Code parcelle']] = 0

print(count)
print(parcelles)

