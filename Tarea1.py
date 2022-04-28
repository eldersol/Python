# -*- coding: utf-8 -*-
import csv
import os

def split_list(lista):
    half = len(lista)//2
    return lista[:half], lista[half:]

with open('data_ids.csv') as archivo:
    contenido = csv.reader(archivo, delimiter=',', quotechar=' ')
    archivo1 = open("suscripcion.sql","w") 
    lista = []

    for linea in contenido:
        lista.append(linea[0])
    
    mitad1, mitad2 = split_list(lista)
    #print(mitad1)
    
    for ids in mitad1:    
        archivo1.write("UPDATE suscripcion SET estado = false WHERE ID=" + str(ids) + ";\n") 
    
    archivo1.close() 


