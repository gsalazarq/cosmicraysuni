import os,fnmatch,subprocess
from math import *
import numpy as np
import time

###### ---------------- #######
def longitud(p_1,p_2):
    x_1 = p_1[0]
    y_1 = p_1[1]
    z_1 = p_1[2]

    x_2 = p_2[0]
    y_2 = p_2[1]
    z_2 = p_2[2]

    long = sqrt((x_1-x_2)**2+(y_1-y_2)**2+(z_1-z_2)**2)

    return long
###### ---------------- #######

###### ---------------- #######
def fgeneral(a,b,c):


    if (b**2 - 4*a*c) < 0:
        raiz_1 = "N/A"
        raiz_2 = "N/A"
        print("no hay raiz real")
    else :
        raiz_1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
        raiz_2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
        print("si hay raiz")

    return raiz_1,raiz_2

###### ---------------- #######


###### ---------------- #######
def norma(a,b,c):

    norm = sqrt(a**2+b**2+c**2)

    return norm
###### ---------------- #######


###### ---------------- #######
def angulo(u_x,u_y,u_z):

    theta = acos(-u_z/(norma(u_x,u_y,u_z)*norma(0,0,-1)))

    return theta

###### ---------------- #######

###### ---------------- #######




def puntos_de_interseccion(u_x,u_y,x_0,y_0, a_p, d_p, ancho, long):
    #r_0 es el punto de inicio de la partícula
    #u_r es el momentum de la partícula
    # el paralelogramo se encuentra en la posición



    definir recta
        definir punto de inicio y pendiente
        #calcular la recta dada un punto y su ángulo
        # 4x + 3y +5z = 2
        # -2x -4y +5z = 2
        #     -8x +8z = 2

        tan(theta)x - y = (bo - tan(theta)*ao)

        A = np.array([tan(theta), -1], [coeficiente de recta 1, coefcieinte de recta 2])
        y = np.array([bo-tan()a0, coeficiente 3])

        alpha = np.linalg.solve(A,y)




    definir los lados como input
    #A (a_p,0) B(a_p+long,0) C(a_p+long,ancho), D(a_p, ancho)
    generar los rectas-lados

    Solucion de intereccion entre recta y lados: alpha y beta
    (x_alpha, y_alpha) = interseccion(recta, lado 1, 2, 4)
        A = np.array([2,4],[8,3])
        y = np.array([2,3])
        x = np.linalg.solve(A,y)


    (x_beta, y_beta) = interseccion(recta, lado 1, 2, 4)


    distancia_atenuacion(beta-alpha)

    Crear vector de solución -> vec_inter = (1 o 0 si cruza 1,1 o 0 si cruza 2, 1 o 0 si cruza 3, 1 o 0 si cruza 4 )

    if  a_p <= x_alpha <= a_p

        guardar cada solución en puntos.



    z_b = -0.6                       #la altura de la tapa del cilindro, -0.6
    z_B = -1.2                       #la altura de la base del cilindro, -1.2
    a_b = z_b/u_z
    a_B = z_B/u_z

    x_b = x_0 + a_b*u_x
    x_B = x_0 + a_B*u_x

    y_b = y_0 + a_b*u_y
    y_B = y_0 + a_B*u_y

    puntos =[]

    if x_b**2 + y_b**2 <= 0.6**2:
        P_b = (x_b,y_b,z_b)
        puntos.append(P_b)    #Punto de entrada
        print("entra por la tapa")
    else:
        P_b = "N/A"
        print("no entra por la tapa")

    if x_B**2 + y_B**2 <= 0.6**2:
        P_B = (x_B,y_B,z_B)
        puntos.append(P_B)   #Punto de salida
        print("sale por la base")
    else:
        P_B = "N/A"
        print("no sale por la base")

    a_ec = u_x**2 + u_y**2
    b_ec = 2*(x_0*u_x+y_0*u_y)
    c_ec = x_0**2 + y_0**2 - 0.6**2

    a_1,a_2 = fgeneral(a_ec,b_ec,c_ec)   #a_1 o a_ corresponden a "a" de entrada o salida

    if a_1 != "N/A" and a_2 != "N/A":
        x_1 = x_0 + a_1*u_x
        x_2 = x_0 + a_2*u_x

        y_1 = y_0 + a_1*u_y
        y_2 = y_0 + a_2*u_y

        z_1 = a_1*u_z
        z_2 = a_2*u_z

        P_1 = "N/A"
        P_2 = "N/A"



        if -1.2<=z_1<=-0.6 :
            P_1 = (x_1,y_1,z_1)
            puntos.append(P_1)
            #print("sale o entra por un lateral z_1")

        if -1.2<=z_2<=-0.6:
            P_2 = (x_2,y_2,z_2)
            puntos.append(P_2)
            #print("entra o sale por un lateral z_2")

        #if (z_1>-0.6 or z_1<-1.2) and (z_2>-0.6 or z_2<-1.2) and  P_b == "N/A" and P_B =="N/A":
            #print("no entra al tanque")

        #if (-1.2<=z_1<=-0.6) or (-1.2<=z_2<=-0.6) or (x_b**2 + y_b**2 <= 0.6**2) or (x_B**2 + y_B**2 <= 0.6**2):
            #print("entra al tanque")



    else:
    #    nic = "N/A"
        print("no entra al tanque 2.0")


    #print(puntos)
    return puntos

###### ---------------- #######

def principal(pattern,root):
    indice = 0

    for path, dirs, files in os.walk(os.path.abspath(root)):
        for filename in sorted(fnmatch.filter(files, pattern)):

            filt_data = []

            oname = "muon_tanque_distancia_"
            oname = oname + str(indice) + ".dat"

            outfile = open(oname,"w")

            print ("processing", filename)


            #raw data
            pname = path + "/" + filename
            fname = filename.split(".")

            #reads the data file
            infile = open(pname,"r")
            data = infile.readlines()
            infile.close()

            for line in data:
                sline = line.split()

                u_x,u_y,u_z,x_0,y_0,z_0 = float(sline[2]),float(sline[3]),float(sline[4]),float(sline[5]),float(sline[6]),float(sline[7])

                Puntos = puntos_de_interseccion(u_x,u_y,u_z,x_0,y_0,z_0)
                theta = angulo(u_x,u_y,u_z)

                if len(Puntos) != 0:
                    a = longitud(Puntos[0], Puntos[1])
                    b = theta*180/pi
                    s = "%s %s" % (a,b)
                    filt_data.append(s)



            for idx in range(len(filt_data)):
                fdata = filt_data[idx].split()

                longitud_recorrida = fdata[0]
                theta = fdata[1]

                s = "%s %s\n" % (longitud_recorrida,theta)
                outfile.write(s)

            outfile.close()
            indice = indice + 1
            data = 0

###############################################################

# main program

principal("muon_lluvia_*.dat","/home/franz/Desktop/Topicos 2/Test-5/")
