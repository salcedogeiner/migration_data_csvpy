import psycopg2
from conf import *

class Connection():
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host

    def get_connection(self):
        #valida parametros
        if not self.dbname:
            print('Parametro name no especificado')
        elif not self.user:
            print('Parametro user no especificado')
        elif not self.password:
            print('Parametro password no especificado')
        elif not self.host:
            print('Parametro host no especificado')

        else:
            #realiza conexion
            if self.connection == None:
                cadena_conect = "dbname={} user={} password={} host={} ".format(self.dbname, self.user, self.password, self.host)
                try:
                    self.connection = psycopg2.connect(cadena_conect)

    		#self.connection.commit()
                except Exception as e:
                    print "I am unable to connect to the database"
                    print e

        return self.connection

    def get_cursor(self):
        if self.cursor == None and self.connection != None:
            self.cursor = self.connection.cursor()
        return self.cursor

#testc = Connection()
#print(testc.user)
#testc.get_connection()
