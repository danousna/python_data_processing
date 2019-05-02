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

null_values = ['None', 'nan']

count_total = 0

sum_val_fonciere = 0
count_val_fonciere = 0

sum_surface_terrain = 0
count_surface_terrain = 0

parcelles = {}
ventes_par_types = {}

for file_name in files:
    gen = read_file_gen(join('compiegne/', file_name))
    for item in gen:
        count_total = count_total + 1

        if item['Valeur fonciere'] != 'None':
            count_val_fonciere = count_val_fonciere + 1
            sum_val_fonciere = sum_val_fonciere + float(item['Valeur fonciere'])

        if item['Surface terrain'] not in null_values:
            count_surface_terrain = count_surface_terrain + 1
            sum_surface_terrain = sum_surface_terrain + float(item['Surface terrain'])

        if item['Code parcelle'] in parcelles.keys():
            parcelles[item['Code parcelle']] = parcelles[item['Code parcelle']] + 1
        else:
            parcelles[item['Code parcelle']] = 0

        if item['Type local'] in ventes_par_types.keys():
            ventes_par_types[item['Type local']]['count'] = ventes_par_types[item['Type local']]['count'] + 1
        else:
            ventes_par_types[item['Type local']]['count'] = 0   

print("Total count: {}".format(count_total))

print("Count Valeur fonciere: {}".format(count_val_fonciere))
print("Moyenne: {}".format(sum_val_fonciere/count_val_fonciere))

print("Count Surface terrain: {}".format(count_surface_terrain))
print("Moyenne: {}".format(sum_surface_terrain/count_surface_terrain))

print(ventes_par_types)
