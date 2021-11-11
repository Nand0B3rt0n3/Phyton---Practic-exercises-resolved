print("Verificacion de aceso")

edad_usuario=int(input("Introduce tu edad, por favor "))

if edad_usuario>100:
	print("Edad incorrecta")
elif edad_usuario<18:
	print("No puedes pasar")
else:
	print("Puedes pasar")
print("Programa finalizado.")

45
print("Verificacion de aceso por nota")

nota_usuario=int(input("Introduce tu nota, por favor "))

if nota_usuario>10:
	print("nota incorrecta")
if nota_usuario<5:
	print("Insuficiente")
if nota_usuario<6:
	print("Suficiente")
if nota_usuario<7:
	print("Bien")
if nota_usuario<9:
	print("Notable")
else:
	print("Sobresaliente")
print("Programa finalizado.")
