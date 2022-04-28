# -*- coding: utf-8 -*-
import csv
import os


with open('data_ids.csv') as archivo:
    contenido = csv.reader(archivo, delimiter=',', quotechar=' ')
    archivo2 = open("Archivo2.sql","w") 
    lista = []
    ids = ""

    for linea in contenido:
        lista.append(linea[0])
    
    for a in range(len(lista)/100) :
        
        for grupo in lista[:99]:
            ids += " ID = " + str(grupo) + " or " 

        ids += " ID = " + str(lista[100])

        archivo2.write("UPDATE suscripcion SET estado = false WHERE " + str(ids) + ";\n")     
    archivo2.close() 


