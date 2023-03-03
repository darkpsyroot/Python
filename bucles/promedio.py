edad = 0
sumaEdad = 0
edadMedia = 0.0
cantidadAlumnosMayores = 0

estatura = 0.0
sumaEstatura = 0.0
estaturaMedia = 0.0
cantidadEstatura = 0

contadorEdad = 0
contadorEstatura = 0



for i in range(5):

    print("Edad alumno ",i+1)
    edad = int(input())
    print("estatura alumno ",i+1)
    estatura = float(input())

    if edad > 0 and edad < 100: 
        if estatura > 0 and estatura < 2.5:
            contadorEdad+=1
            contadorEstatura+=1
            sumaEdad += edad
            sumaEstatura += estatura
            if (edad > 18): 
                cantidadAlumnosMayores+=1    
            if (estatura == 1.75):
                cantidadEstatura+=1

edadMedia = sumaEdad / contadorEdad
estaturaMedia = sumaEstatura / contadorEstatura

print("Edad media: ", edadMedia, "/n")
print("Estatura media: ", estaturaMedia, "/n")
print("Alumnos mayores de 18: ", cantidadAlumnosMayores,"/n")
print("Alumnos que miden 1.75: ", cantidadEstatura)


