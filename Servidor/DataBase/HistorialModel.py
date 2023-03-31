from DataBase.conexion import Data

class HistorialModel:
    def __init__(self):
        self.DataBase=Data()

    def select (self):
        query = '''
        SELECT HISTORIAL.HORA, Usuario.NOMBRE, SEMAFORO.NOMBRE,SEMAFORO.IP,HISTORIAL.ETSADO
	        FROM USUARIO_R_SEMAFORO_R_HISTORIAL AS U_R 
		        INNER JOIN HISTORIAL ON HISTORIAL.ID = U_R.ID_HISTORIAL
		        INNER JOIN Usuario on Usuario.ID = U_R.ID_USUARIO
		        INNER join SEMAFORO on SEMAFORO.ID = U_R.ID_SEMAFORO
        '''
        self.lista=[]
        for row in self.DataBase.Selecionar(query):
            obj =  {"Hora":row[0],"Nombre Usuario":row[1] , "Nombre Semaforo":row[2],"IP Semaforo":row[3],"Estado Semaforo":row[4]}
            self.lista.append(obj)
        return self.lista
    
    def insert(self,HORA, ETSADO):
        query='INSERT INTO "Historial"("HORA","ETSADO") VALUES ("'+HORA+'","'+ETSADO+'")'
        print(self.DataBase.Modificar(query))
    
    def Delet(self,ID_HISTORIAL,ID_SEMAFORO,ID_USUARIO):
        query='DELETE FROM "USUARIO_R_SEMAFORO_R_HISTORIAL" WHERE "ID_HISTORIAL" = '+str(ID_HISTORIAL)+' AND "ID_SEMAFORO"= '+str(ID_SEMAFORO)+' AND "ID_USUARIO"= '+str(ID_USUARIO)
        print(self.DataBase.Modificar(query))

    def insert_R(self,ID_HISTORIAL,ID_USUARIO,ID_SEMAFORO):
        query='INSERT INTO "USUARIO_R_SEMAFORO_R_HISTORIAL"("ID_HISTORIAL","ID_USUARIO","ID_SEMAFORO") VALUES ("'+ID_HISTORIAL+'","'+ID_USUARIO+'","'+ID_SEMAFORO+'")'
        print(self.DataBase.Modificar(query))