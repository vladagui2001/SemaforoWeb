import sqlite3
from DataBase.config import server

class Data:

    def Selecionar(self,query):
        try:
            con = sqlite3.connect(server)
            cur = con.cursor()
            table= cur.execute(query)
            return table
        except Exception as err:
            return "Eroor: "+str(err)+""+str(type(err))


    def Modificar(self,query):
        try:
            con = sqlite3.connect(server)
            cur = con.cursor()
            cur.execute(query).fetchall()
            con.commit()
            cur.close()
            con.close()
            return "Ok"
        except Exception as err:
            if "<class 'sqlite3.OperationalError'>" == str(type(err)):
                return "Eroor: "+str(err)+""+str(type(err)) +"""
                Recomendacion: Verivique que solo tenga una intacia con la base de datos abierta ya sea 
                    1.- Codigo, asegurate de usar cur.close(), con.close()
                    2.- otros progamas que tengan aseso a ella 
                    3.- Verifica tu consulta sql
                Solo un proseso o progma a la ves 
                """
            else:
                return "Eroor: "+str(err)+""+str(type(err)) 
        

