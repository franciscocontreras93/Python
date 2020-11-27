from configparser import ConfigParser
#from cryptography.fernet import Fernet


class Configuracion:
    def __init__(self):
        self.fileOpen = open('files//bd_config.cfg')
    def create(self):
        self.file = self.fileOpen
        self.section = 'prototipo'
        self.dbName = input("Nombre de la base de Datos: ")
        self.dbUser = input("Usuario de Base de Datos: ")
        self.dbPass = input("Password de Base de Datos: ")
        self.dbHost = input("Host: ")
        self.dbPort = input("Port: ")        
        self.parser = ConfigParser()
        self.parser.add_section(self.section)
        self.parser.set(self.section, 'dbname', self.dbName)
        self.parser.set(self.section, 'user', self.dbUser  )
        self.parser.set(self.section, 'password', self.dbPass)
        self.parser.set(self.section, 'host', self.dbHost)        
        self.parser.set(self.section, 'port', self.dbPort)
        self.parser.write(self.file)
        self.file.close()
    def config(self):
        self.fileOpen
        parser = ConfigParser()
        parser.read_file(self.fileOpen)
        section = 'prototipo'
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]       
        self.fileOpen.close
        return db
    def config2(self):
        self.fileOpen
        parser = ConfigParser()
        parser.read_file(self.fileOpen)
        section = 'conexion_2'
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        self.fileOpen.close
        return db
    def readFile(self):
        parser = ConfigParser()
        parser.read('files//bd_config.cfg')
        for section_name in parser.sections():
            print('Section:', section_name)
            print('  Options:', parser.options(section_name))
            for name, value in parser.items(section_name):
                print('  {} = {}'.format(name, value))
            print()
    def modifyUser(self,idUsuario):      
        parser = ConfigParser()
        parser.read("files//bd_config.cfg")
        """ IMPRESION DE DATOS DE CONFGIG """
        """ print('Read values:\n')
        for section in parser.sections():
            print(section)
            for name, value in parser.items(section):
                print('  {} = {!r}'.format(name, value))
        #parser.remove_option('conexion_2', 'user') """
        parser.set('conexion_2','user',idUsuario)
        with open("files//bd_config.cfg", 'w') as configfile:
            parser.write(configfile)
        """ IMPRESION DE ERSULTADOS DE MODIFICACION DE CONFGIG """
        """ print('\nModified values:\n')
        for section in parser.sections():
            print(section)
            for name, value in parser.items(section):
                print('  {} = {!r}'.format(name, value)) """


        





 
        

