# Una historia de usuario es un pedido por el cual se solicita
# una mejora u actualización de un programa determinado.
 
# La historia de usuario sirve para mejorar la calidad del producto
# o servicio brindado, también para medir la dificultad que dicha
# mejora tendrá. 

# Un ejemplo sería el siguiente:

# Historia: Promedio de notas
# Como estudiante de la USIL me gustaría saber cual sería mi 
# promedio al finalizar el curso para poder garantizar que me 
# podré matricular en un curso lo cual este es su pre-requisito

pc1=int(input("ingrese la nota de la pc1"))
pc2=int(input("ingrese la nota de la pc2"))
trabajo=int(input("ingrese la nota del trabajo"))
expar=int(input("ingrese la nota del parcial"))
exfi=int(input("ingrese la nota del final"))

promprac=(((pc1+pc2)*0.5))*0.6
trab=trabajo*0.4
prom=(promprac+trab)*0.5
par=expar*0.25
fin=exfi*0.25

notafinal=prom+par+fin

print(notafinal)

if notafinal>10:
    print("Aprobó el curso")
else:
    print("Desaprobó el curso")
