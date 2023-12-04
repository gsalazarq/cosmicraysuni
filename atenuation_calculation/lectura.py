import csv
import numpy as np
import pandas as pd
import math


# Especifica la ruta de tu archivo CSV
archivo_csv = '/media/justus/C063-5C5D/lim-2201-01_086400.shw'

 
m_rest=0.1057 #unit: GeV/c**2

vector = []
# Abre el archivo CSV en modo lectura
with open(archivo_csv, 'r') as archivo:
    # Crea un objeto lector de diccionario CSV
    lineas = archivo.readlines()


    # Itera sobre cada línea del archivo
    for linea in lineas[0:6000]:
        # Elimina los caracteres de salto de línea y divide los valores por espacios
        valores = linea.strip().split()

        # Imprime solo el primer valor (primera columna)
        if len(valores) > 0:
            #if valores[0] == '0005' or valores[0] == '0006': 
                #print(int(valores[0]), valores[1], valores[2], valores[3], valores[4], valores[5], valores[6], valores[7], valores[8], valores[9], valores[10], valores[11])
            pt=np.sqrt(float(valores[1])**2 + float(valores[2])**2+ float(valores[3])**2)
            Et=np.sqrt(pt**2+m_rest**2)
            thetat=round(90-np.degrees(np.arccos(float(valores[3])/pt)) )#theta ya esta en grados

            at2=math.atan(float(valores[2])/float(valores[1]))
            phit=np.round(np.degrees((2*np.pi+at2)*(at2<0)+(at2)*(at2>0)))

            vector.append([valores[0], phit, thetat, Et])


ruta_archivo_salida = './data/energia_2_temp.txt'
df = pd.DataFrame(vector, columns=['part','phit','thetat', 'Et'])
     
df.to_csv(ruta_archivo_salida, index=False, header=True, sep=' ') 
     

  
