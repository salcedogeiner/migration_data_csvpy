from arbol_cuentas import ArbolCuentas
from conf import *

def main():

    filedata=raw_input("Ingrese la ruta del data: \n")
    idplan=int(input("Ingrese el id del plan de cuentas: \n"))
    #print(filedata)

    load = ArbolCuentas()
    load.reg_rel(filedata,idplan)


if __name__ == '__main__':
	main()
