import random
var_n = int(input("Ingrese la dimesion de la matriz cuadrada: "))
while var_n <= 1 :
 	print("\n Error la dimension debe ser mayor a 1")
 	var_n = int(input("\nIngrese la dimesion de la matriz cuadrada: "))

matriz = []

for i in range(1,var_n + 1):
	lista = []
	matriz.append(lista)
	for j in range(1,var_n + 1) :
		elemento_ij = random.randrange(i,2 * i + i*j)
		lista.append(elemento_ij)
		
print(matriz)
