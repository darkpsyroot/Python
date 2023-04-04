edad = 28
estatura = 1.65

if edad > 0 & edad < 100:
    print(edad)

if edad > 0 & edad < 100:
    if estatura > 0.0 and estatura < 2.5:
        print(estatura)

for i in range(5):
    if edad > 0 & edad < 100:
        if estatura > 0.0 and estatura < 2.5:
            print(estatura," ",i)

contador = 0
sumaEdad = 0
edadMedia = 0.0
for i in range(5):
    if edad > 0 & edad < 100:
        contador +=1
        sumaEdad += edad
edadMedia = sumaEdad / contador
        