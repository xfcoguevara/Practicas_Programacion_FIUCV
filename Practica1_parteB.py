#inicio del programa
#distancia entre dos puntos 
#Hallar las coordenadas del punto medio
import math
Var_x = float(input("Ingrese la coordena X del punto Inicial: "))
Var_y = float(input("Ingrese la coordena Y del punto Inicial: "))
Var_x1 = float(input("Ingrese la coordena X del punto Final: "))
Var_y1 = float(input("Ingrese la coordena Y del punto Final: "))

Var_distancia = math.sqrt((Var_x1 - Var_x)**2 + (Var_y1 - Var_y)**2)
CoordenadaPm_x = (Var_x + Var_x1) / 2
CoordenadaPm_y = (Var_y + Var_y1) / 2


print("\nLa distancia entre los puntos es: {}".format(Var_distancia))

print("\nLas coordenas del puntos medio son: {} , {}".format(CoordenadaPm_x,CoordenadaPm_y))

