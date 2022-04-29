# -*- coding: utf-8 -*-
import csv
import os

def split_list(lista):
    half = len(lista)//2
    return lista[:half], lista[half:]

with open('data_ids.csv') as archivo:
    contenido = csv.reader(archivo, delimiter=',', quotechar=' ')
    archivo1_1 = open("Archivo1_1.sql","w") 
    archivo1_2 = open("Archivo1_2.sql","w") 
    lista = []

    for linea in contenido:
        lista.append(linea[0])
    
    mitad1, mitad2 = split_list(lista)
    #print(mitad1)
    
    for ids in mitad1:    
        archivo1_1.write("UPDATE suscripcion SET estado = false WHERE ID=" + str(ids) + ";\n") 

    for ids in mitad2:    
        archivo1_2.write("UPDATE suscripcion SET estado = false WHERE ID=" + str(ids) + ";\n") 
    
    archivo1_1.close() 
    archivo1_2.close() 


