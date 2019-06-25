
import random

a=[]
x=0
while True:

    n=int(input("Escoja un número entre 1 y 10: "))
    if n>=1 and n<=10:
        a.append(n)
        x=x+1
        if x==6:
            break
    else:
        print("¡Escoja un número entre 1 y 10!")

c=[]

for i in range(6):
    b=random.randint(1,10)
    
    c.append(b)
print(c)
print(a)

y=0
for i in range(6):
    for j in range(6):
        if c[i]==a[j]:
            y=y+1
print("Has acertado ",y," números")

if y==6:
    print("Has ganado 6 millones de soles")
elif y==5:
    print("Ha ganado 100 mil soles")
else:
    print("Siga intentando")

                