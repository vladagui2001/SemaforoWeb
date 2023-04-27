from conexion import Data

class Permisos_R_Usuarios:
    def __init__(self):
        self.DataBase=Data()

    def select (self):
        query = '''
        SELECT Usuario.NOMBRE,PERMISOS.NOMBRE 
            FROM USARIO_R_PERMISO
                INNER JOIN Usuario on 
                    Usuario.ID = USARIO_R_PERMISO.ID_USUARIO  
                INNER JOIN PERMISOS on 
                    PERMISOS.ID = USARIO_R_PERMISO.ID_PERMISO
        '''
        self.lista=[]
        for row in self.DataBase.Selecionar(query):
            obj =  {"Usuario":row[0],"Permiso":row[1]}
            self.lista.append(obj)
        return self.lista
    
    def insert(self,Id_Usuario,Id_Permiso):
        query='INSERT INTO "main"."USARIO_R_PERMISO"("ID_USUARIO","ID_PERMISO") VALUES ("'+Id_Usuario+'","'+Id_Permiso+'")'
        print(self.DataBase.Modificar(query))
    
    def Delet(self,id_Usario,id_permiso):
        query='DELETE FROM "main"."USARIO_R_PERMISO" WHERE "ID_USUARIO"='+str(id_Usario)+'AND "ID_PERMISO"='+str(id_permiso) 
        print(self.DataBase.Modificar(query))