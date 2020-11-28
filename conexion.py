import psycopg2
from config import Configuracion

class Conexion:
    def __init__(self):       
        self.modelo = Configuracion()        
        self.loginStatus = False    
        self.idUser = None
        self.usuario = input("Ingrese su Usuario: ")
        self.password = input("Ingrese su Password: ")
        self.login()        
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
        try:
            print("Intentando Conectar...")
            conn = self.conexionPrimaria()
            cursor = conn.cursor()                      
            query = """SELECT * FROM cmg.cmg_usuarios_sstma WHERE id_usuario = '%s'  AND clave_qgis = '%s'""" % (self.usuario, self.password)
            cursor.execute(query)
            rows = cursor.fetchall()
            result = cursor.rowcount            
            if result == 1 and self.loginStatus== False:
                for row in rows: 
                    self.idUser = row[17] # PASARLO COMO PARAMETRO A LA CONEXION 2
                    nameUser = row[9]
                    lastnameUser = row[1]
                print("Conexion Exitosa Bienvenido")                              
                self.loginStatus = True
            else: 
                print("Usuario o Password Incorrecta")
            return self.loginStatus               
        except psycopg2.Error as e:            
            error_code = e.pgcode
            print(error_code)
            print("Ocurrio un error en la Conexion")
        
    def accion(self, userDb):
        modelo = Configuracion()
        params = modelo.config()
        if self.loginStatus != False:      
            conn = modelo.conexionSecundaria(userDb)
            cur = conn.cursor()
            cur.execute("SELECT id_usuario FROM cmg.cmg_usuarios_sstma")
            resultado = cur.fetchall()          
            for elemento in resultado:         
                print(elemento)       
        
    def conexionPrimaria(self):
        stringConexion = "dbname='prototipo' user='cmg_toolbox' host='181.143.104.82' password='23826405'"
        try:            
            conn = psycopg2.connect(stringConexion)
            self.conexionStatus = True            
        except:
            print("Imposible Conectar")
        return conn

model = Conexion()



        

