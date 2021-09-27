#Entrada del número que se quiere convertir en binario en el sistema decimal
decimal=int(input("Introduce un número sin decimales para convertirlo en binario: "))

#Creamos una nueva variable llamada "division" para conservar el número en el sistema decimal, ya que lo mostraremos en el resultado
division=decimal
binario=0
cont=0

#Calculamos la conversión a binario mediante la división entera. Este proceso de cálculo queda representado en la fotografía explicativa 
#que se encuentra en la misma carpeta de esta tarea
while division>0:
    binario+=(division%2)*(10**cont)
    division//=2
    cont+=1

print(f"El número {decimal} en binario es {binario}")
