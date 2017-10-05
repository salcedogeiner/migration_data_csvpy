from bdConnection import Connection
import csv

class ArbolCuentas:

    def reg_rel(self,myfile,id_plan):
        try:
            connectdb = Connection()
            connect = connectdb.get_connection()

            #x = cursor.fetchone()
            #print(x)
            with open(myfile, 'rb') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if len(row["Codigo"])>1:
                        row["Codigo"]=row["Codigo"][0]+"-"+row["Codigo"][1:]
                    print row["Codigo"],row["Nombre"]
                    cursor = connectdb.get_cursor()
                    cursor.execute(""" SELECT cuenta_padre, cuenta_hijo
                    FROM financiera.estructura_cuentas e
                    INNER JOIN financiera.cuenta_contable c
                    ON c.codigo=%s and c.id = e.cuenta_hijo
                    and plan_cuentas = 2;""",(row["Codigo"],))  #plan de cuentas maestro
                    #cursor.execute(""" INSERT INTO financiera.estructura_cuentas VALUES (null,%s,%s,%s)""",(row["idCuenta"],row["idPadre"],id_plan))
                    x = cursor.fetchone()
                    if x != None:
                        cursor.execute(""" INSERT INTO financiera.estructura_cuentas (cuenta_padre, cuenta_hijo, plan_cuentas) VALUES (%s,%s,%s)""",(x[0],x[1],id_plan,))
                        print(x[0])
                        print(x[1])
                        cursor.statusmessage
        except Exception as error:
            connect.rollback()
            print(error)
        finally:
            if connect is not None:
                connect.commit()
                connect.close()


#test = ArbolCuentas()

#test.reg_rel("sone")
