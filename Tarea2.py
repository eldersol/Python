# -*- coding: utf-8 -*-
import csv
import os


with open('data_ids.csv') as archivo:
    contenido = csv.reader(archivo, delimiter=',', quotechar=' ')
    archivo2 = open("Archivo2.sql","w") 
    lista = []
    

    for linea in contenido:
        lista.append(linea[0])
    
    for x in range(len(lista)/100):
        ids = ""
        g100=[]

        for grupo in lista[x*100:(x*100)+100]:
            g100.append(grupo)
        
        for id in g100:
            ids += " ID = " + str(id) + " or " 
        
        ids += " ID = " + str(g100[99])        
        archivo2.write("UPDATE suscripcion SET estado = false WHERE " + str(ids) + ";\n")     
    
    archivo2.close() 


