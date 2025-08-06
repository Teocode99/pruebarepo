print("\nCalcula tu promedio, ingresa tus calificaciones")
calificacion = 1
promedio = 0
contador = 0
while calificacion > 0:
    calificacion = int(input("escribe tu calificacion"))
    promedio = calificacion + promedio 
    contador = contador + 1
print ("Tu promedio es:",promedio/contador)
