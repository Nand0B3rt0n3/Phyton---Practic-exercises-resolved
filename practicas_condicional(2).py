print("Programa de becas Año 2021")
distancia_escuela=int(input("introduce la distancia en km "))
print(distancia_escuela)

numero_hermanos=int(input("Introduce el nº de hermanos en el centro "))
print(numero_hermanos)

salario_familiar=int(input("introduce salario anual bruto "))
print(salario_familiar)

if distancia_escuela>40 and numero_hermanos>2 and salario_familiar<=20000:
	print("Tienes derecho a beca")

else:
	print("No tienes derecho a beca")