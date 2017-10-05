import csv
def leer_csv():
    with open('resultadoCargueC.csv', 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print row["idCuenta"],row["idPadre"]




leer_csv()
