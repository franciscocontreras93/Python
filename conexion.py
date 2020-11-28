import psycopg2
from config import Configuracion

class Conexion:
    def __init__(self):       
        self.modelo = Configuracion()        
        
        self.usuario = input("Ingrese su Usuario: ")
        self.password = input("Ingrese su Password: ")
        self.login()

    def configConexion(self):
        self.modelo = Configuracion()
        self.modelo.create()
    
    def login(self):
        
        modelo = Configuracion()
        params = modelo.config()
        print("Intentando Conectar")
        try:           
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            # UNCOMENT FOR DEBUG 
            #print("La version de BD es: ")
            query = """SELECT * FROM cmg.cmg_usuarios_sstma WHERE id_usuario = '%s'  AND clave_qgis = '%s'""" % (self.usuario, self.password)
            cur.execute(query)
            rows = cur.fetchall()
            result = cur.rowcount
            if result == 1 :                
                for row in rows: 
                    idUser = row[17] # PASARLO COMO PARAMETRO A LA CONEXION 2
                    nameUser = row[9]
                    lastnameUser = row[1]
                print("Welcome ", nameUser, lastnameUser, "su usuario es: ", idUser)
                print(result)
                modelo.modifyUser(idUser)
            else:
                print(result)
                print("User or password Incorrect")
            
            
            return conn      
        except:
            print("Ocurrio un error en la Conexion")

        
     

model = Conexion()



        

