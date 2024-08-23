import csv

with open("archivos//datos.csv") as mycsv:
    leido = csv.reader(mycsv)
    for row in leido:
        print(row)

