import psycopg2
from config import Configuracion

class Conexion:
    def __init__(self):       
        self.modelo = Configuracion()        
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
            cur.execute("SELECT * FROM cmg.cmg_usuarios_sstma WHERE id_usuario = 'HMONTOYA'  AND clave_qgis = '12345'")
            rows = cur.fetchall()
            result = cur.rowcount
            if result == 1 :                
                for row in rows: 
                    idUser = row[0]
                    nameUser = row[9]
                    lastnameUser = row[1]
                print("Welcome ", nameUser, lastnameUser)
            else: 
                print("User or password Incorrect")
            
            print(result)
            return conn      
        except:
            print("Ocurrio un error en la Conexion")
model = Conexion()


        

