import random

var_n = int(input("Ingrese el numero de filas de la matriz: "))
var_m = int(input("Ingrese el numero de columnas de la matriz: "))

while var_n <= 1 or var_m <=1 :
 	if var_n <= 1:
 		print("\n Error el numero de filas debe ser mayor a 1")
 	if var_m <=1 :
 		print("\n Error el numero de columnas debe ser mayor a 1")
 	var_n = int(input("\nIngrese la dimesion de la matriz cuadrada: "))

matriz_1 = []

for i in range(0,var_n):
	lista_1 = []
	matriz_1.append(lista_1)
	for j in range(0,var_m) :
		elemento_ij = random.randrange(2,4)
		lista_1.append(elemento_ij)

matriz_2 = []

for i in range(0,var_m):
	lista_2 = []
	matriz_2.append(lista_2)
	for j in range(0,var_n) :
		elemento_ij = random.randrange(2,4)
		lista_2.append(elemento_ij)
import copy
matriz_1a = copy.deepcopy(matriz_1)
matriz_2a = copy.deepcopy(matriz_2)

def expmatriz(n,m,matriz):
	for i in range(0,n):
		for j in range(0,m):
			matriz[i][j] = str(matriz[i][j])
	for n in range(0,n):
		var =  print(" ".join(matriz[n]))
	return var

print("\nLa matriz A es: ")
print()
expmatriz(var_n,var_m,matriz_1a)

print("\nLa matriz B es: ")
print()
expmatriz(var_m,var_n,matriz_2a)

matriz_3 = []

for i in range(0,var_n):
	lista_3 = []
	matriz_3.append(lista_3)
	for j in range(0,var_n) :
		lista_3.append(0)


ij = 0
for h in range(0,var_n):
	
	for k in range(0,var_m):
		
		for l in range(0,var_n):
			ij = matriz_1[h][k] * matriz_2[k][l]
			matriz_3[h][l] = matriz_3[h][l] + ij 


print("\nLa matriz C es el producto de A por B")
print()
expmatriz(var_n,var_n,matriz_3)










