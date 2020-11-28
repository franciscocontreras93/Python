import os
import csv

directorio = "F:/FRANCISCO/GIS/ISMAEL/BASES 2020/ENVIAR/verificar"
archivos = []
archivo = open('lista.txt', 'wb')

for file in os.listdir(directorio):
    if file.endswith(".xlsx"):
        archivos.append(file) 
        print(file)
