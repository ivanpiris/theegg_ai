#Entrada del número decimal. Este algoritmo funciona para cualquier número y no sólo los comprendidos entre 0 y 1.

decimal=input("Introduce un número decimal: ")

#Convertimos la entrada en fracción de la siguiente manera: Si la entrada es 0.25 el numerador será 0.25 por 10^2 (25) y el denominador sería 10^2. 
#Mantenemos numerador y denominador por separado para poder operar con ellos como si fuesen números enteros.

num=int(float(decimal)*(10**(len(decimal)-2)))
denom=10**(len(decimal)-2)
i=2

#Ahora el algoritmo dividirá tanto numerador como denominador por el mismo divisor (siempre que el resto sea cero) 
#hasta llegar a un divisor > que la mitad del numerador o denominador. 

while (i<=num/2 and i<=denom/2):
    while (num%i==0 and denom%i==0):
        num//=i
        denom//=i
        
    i+=1

    
#Cuando sale del bucle solo queda por comprobar que no se pueden dividir ambos por el valor del numerador o denominador.

if num%denom==0:
    num,denom=(num//denom),1
    
    
elif denom%num==0:
    denom,num=(denom//num),1
    
print(f"La fracción irreducible es: {num}/{denom}")
