#inicio del programa
#convertir una coordenada cartesiana a polar
# r = distancia
#an = angulo en del eje x al vector en sentido anti horario

#Recoleccion de datos
import math
Var_x = float(input("Ingrese la coordenada X del punto: "))
Var_y = float(input("Ingrese la coordenada Y del punto: "))
Var_r = math.hypot(Var_x,Var_y)
print()

#procedimientos

if Var_r == 0 :

	print("La distancia es: {}".format(0))
	print()
	print("El angulo es: {} Grados".format(0))
	print()
	print("El punto se encuentra en el origen")

else:
	print("La distancia es: {} ".format(Var_r))
	print()

	if Var_x == 0 :

		if Var_y > 0 :
			print("El angulo es: {} Grados".format(90))
		else :
			print("El angulo es: {} Grados".format(270))

	if Var_x > 0 :

		if Var_y >= 0 :
			Var_an = math.degrees(math.atan(Var_y / Var_x))
			print("El angulo es: {} Grados".format(Var_an))
		else :
			Var_an = abs(math.degrees(math.atan(Var_y / Var_x))) + 270	
			print("El angulo es: {} Grados".format(Var_an))

	if Var_x < 0 :

		if Var_y > 0 :
			Var_an = abs(math.degrees(math.atan(Var_y / Var_x))) + 90	
			print("El angulo es: {} Grados".format(Var_an))
		else :
			Var_an = abs(math.degrees(math.atan(Var_y / Var_x))) + 180	
			print("El angulo es: {} Grados".format(Var_an))


