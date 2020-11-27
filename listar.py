import os
import csv

directorio = "C:/Users/FRANCISCO/Downloads/Telegram Desktop"
archivos = []
archivo = open('lista.txt', 'wb')

for file in os.listdir(directorio):
    if file.endswith(".xlsx"):
        archivos.append(file) 
        print(file)
