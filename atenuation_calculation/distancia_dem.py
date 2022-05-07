import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd


## línea de visión
def recta(x_0, y_0, x_1,y_1,x): # todos los puntos son conocidos, la función bota un punto adelante
    m=(y_1-y_0)/(x_1-x_0)
    recta= y_0+m*(x-x_0)

    return recta

def segmentos(array1, array2):  # primero los valores y de la curva
    vect = []
    index = []
    for i in range(0,len(array1)):
        if (array1-array2)[i] >= 0: #la condicion.
            vect.append(array1[i])
            index.append(i)
    #    else:
     #       vect.append(0)
      #      index.append(0)
    return (index, vect)

#### SUPER IMPORTANTE
def indice_final(array1, array2):  # genera el index final de intersección
    for i in range(inicio,len(array1)):
        if (array1-array2)[i] >= 0: #la condicion.
            indice_final=i
    return indice_final

#funcion para calcular la distancia entre dos puntos
# p1 y p2 son array de dos dimensiones  que tiene los puntos (x,y)

def distancia(p1, p2): #la entrada
    resto = p2**2-p1**2
    dist = math.sqrt(abs(resto[0])+ abs(resto[1]))
    return dist


#Lectura del archivo

df = pd.read_csv('./rastert_dem_uni1-clean.txt', sep =" ", header=None)
df_filtrado = df.fillna(0)
df_limpio=df.drop(columns=626)#eliminar la última columna
#df_limpio.head()


#array con los valores de X que depende de el número de celdas que tiene la información GIS
# el valor real debe salir de df_limpio.shape[1]
len_colum = df_limpio.shape[1]
len_filas = df_limpio.shape[0]
arr_x = np.linspace(0,len_colum-1,len_colum)

#### IMPORTANTE
inicio = 380 # indice donde quiero empezar a analizar en el eje X

punto_inicio=[50,120]# punto desde donde se coloca el observador

####  Puntos de la curva
# iloc 110 elige la fila que quiero analizar

np_array = df_limpio.iloc[110].to_numpy()

vec_recta= []

#esto genera la recta
for j in range(0,len(arr_x)):
    tm=recta(punto_inicio[0],punto_inicio[1],arr_x[inicio], np_array[inicio], arr_x[j])
    vec_recta.append(tm)
    recta_vec = np.asarray(vec_recta)

plt.ylim([70, 250]) # limita el rango en el que se muestra el eje Y
plt.plot(recta_vec)
plt.plot(np_array)

len(np_array)
print(arr_x[inicio])
print(np_array[inicio])


#cálculo de la distancia




lf= indice_final(np_array, recta_vec) # indice final de intersección  # PUNTO 2 P2

int_i= np.asarray([inicio,np_array[inicio]])#convertir los puntos iniciales en el  array  PUNTO DE INICIO P1
int_f= np.asarray([lf,np_array[lf]])#convertir los puntos finales en el  array
u = distancia(int_i, int_f) #cacula la distancia
print(f"Distancia: {u}")

plt.show()
