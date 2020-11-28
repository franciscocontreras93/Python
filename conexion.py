import psycopg2
from config import Configuracion

class Conexion:
    def __init__(self):       
        self.modelo = Configuracion()
        self.loginStatus = False       
        print(self.loginStatus)
        self.idUser = None
        self.usuario = input("Ingrese su Usuario: ")
        self.password = input("Ingrese su Password: ")
        self.login()
        #print(self.idUser)
        try:
            self.accion(self.idUser)
        except psycopg2.Error as e:
            error_code = e.pgcode
            if error_code == "42501":
                print("Su usuario no tiene los permisos necesarios,\ncomuniquese con el Gestor del Sistema")

    def configConexion(self):
        self.modelo = Configuracion()
        self.modelo.create()
    
    def login(self):
        
        modelo = Configuracion()
        params = modelo.config()
        print("Intentando Conectar...")
        try:           
            conn = modelo.conexionPrimaria()
            cur = conn.cursor()
            # UNCOMENT FOR DEBUG 
            #print("La version de BD es: ")
            query = """SELECT * FROM cmg.cmg_usuarios_sstma WHERE id_usuario = '%s'  AND clave_qgis = '%s'""" % (self.usuario, self.password)
            cur.execute(query)
            rows = cur.fetchall()
            result = cur.rowcount
            
            if result == 1 and self.loginStatus== False:

                for row in rows: 
                    self.idUser = row[17] # PASARLO COMO PARAMETRO A LA CONEXION 2
                    nameUser = row[9]
                    lastnameUser = row[1]

                print("Conexion Exitosa")
                print("Bienvenido ", nameUser, lastnameUser)
                #print(result)
                self.loginStatus = True
                modelo.modifyUser(self.idUser) 
                #print(self.loginStatus)
                           
            else:
                #print(result)
                print("Usuario o Password Incorrecta")
            
            
            return self.loginStatus
                       
        except:
            print("Ocurrio un error en la Conexion")
        
    def accion(self, userDb):
        modelo = Configuracion()
        params = modelo.config()
        
        if self.loginStatus != False:
                    
            conn = modelo.conexionSecundaria(userDb)
            cursor = conn.cursor()
            cursor.execute("SELECT id_usuario FROM cmg.cmg_usuarios_sstma")
            resultado = cursor.fetchall()          
            for elemento in resultado:         
                print(elemento)       
        
     

model = Conexion()



        

