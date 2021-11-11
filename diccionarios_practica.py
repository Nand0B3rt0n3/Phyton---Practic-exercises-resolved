#Creando diccionario
midiccionario={"Alemania":"Berlin","Francia":"Paris","Reino Unido":"Londres", "España":"Madrid"}

#Agregando elementos al diccionario
midiccionario["Italia"]="Lisboa"
print(midiccionario)

#Correccion de elementos existentes
midiccionario["Italia"]="Roma"
print(midiccionario)

#Eliminar elementos existentes
del midiccionario["Reino Unido"]
print(midiccionario)

#--------------------------------

mitupla=["España", "Reino unido", "Francia", "Alemania"]
midiccionario={mitupla[0]:"Madrid", mitupla[1]:"Londres", mitupla[2]:"Paris", mitupla[3]:"Berlin"}
print(midiccionario)
#imprime cuantos valores hay almacenados en la lista
print(len(mitupla))