#convertir una cantidad se segundos en a;os,meses,dias,horas,minutos y segundos
#1 a;no = 360 dias
#todos los meses son de 30 dias
#inicio del programa


Var_seg =int(input('Ingrese la una cantidad de segundos: '))

#calculo de los a;nos: 1 a;o = 31104000 segundos
Var_an = (Var_seg // 31104000)

	#Segundos restantes 1 son:
Var_seg = Var_seg - (Var_an * 31104000)

# calculo de los meses: 1 mes = 2592000 segundos
Var_mes = Var_seg // 2592000

	#Segundos restantes 2 son:
Var_seg = Var_seg - (Var_mes * 2592000)

Var_dia = Var_seg // 86400

 	#Segundos restantes 3 son:
Var_seg = Var_seg - (Var_dia * 86400)

# Calculo de las horas
Var_hr = Var_seg // 3600

	#segundos restantes 4:
Var_seg = Var_seg - (Var_hr * 3600)

#Calculo de los minutos
Var_min = Var_seg // 60

#Calculo de los Segundos:
Var_seg = Var_seg - (Var_min * 60)

Lista_1 = [Var_an,Var_mes,Var_dia,Var_hr,Var_min,Var_seg]


Lista_2 = ["{} a#os".format(Var_an),"{} meses".format(Var_mes),"{} dias".format(Var_dia),"{} horas".format(Var_hr),"{} minutos".format(Var_min),"{} segundos".format(Var_seg)]



for i in [5,4,3,2,1,0]:

	if Lista_1[i] == 0 : #condicion para eliminar los datos que sean 0 ej: 0 mes
		ind = Lista_1.index(0)
		#Lista_1.pop(ind)
		Lista_2.pop(ind)

	elif Lista_1[i] == 1 : #Condicion para definir la singularidad de las palabras a#o,mes,hora,dia,minuto y segundo

		if i == 1 : #Condicion especial para la palabra mes(se deben eliminar Las dos ultimas letras para pasar de plural a singular)
			Lista_4 = list(Lista_2[1])
			Lista_4.pop()
			Lista_4.pop()
			Lista_4 = "".join(Lista_4)
			Lista_2[1] = Lista_4

		else : # a#o,dia,hora,minuto,segundo
			Lista_3 = list(Lista_2[i])
			Lista_3.pop()
			Lista_3 = "".join(Lista_3)
			Lista_2[i] = Lista_3
		
	
print("\nLa cantidad de segundos ingresados es equivalente a:\n ")
print(", ".join(Lista_2)) #joint convierte una lista en un string


		









 



	












