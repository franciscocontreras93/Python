class Entrevista:
    def __init__(self):
        print("por que el color verde del aguacate?: ")
        self.respuesta()

    def respuesta(self):
        self.respuesta = input("Ingrese la respuesta: ")
        if self.respuesta == "no se":
            print("potaxio")
        else:
            print(self.respuesta)


model = Entrevista()

