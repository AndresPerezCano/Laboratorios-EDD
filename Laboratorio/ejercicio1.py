#daniel_zapata.005
indice = int(input("Ingrese un numero entero: "))

listaNumeros = []

while indice > 0:
    numero = int(input("Ingrese un numero entero: "))
    listaNumeros.append(numero)
    indice -= 1

valorMaximo = 0
valorMinimo = 0
promedio = 0

for i in listaNumeros:
    if valorMaximo == 0 and valorMinimo == 0:
        valorMaximo = i
        valorMinimo = i
        promedio += i

    elif i >= valorMaximo:
        valorMaximo = i
        promedio += i

    elif valorMinimo >= i:
        valorMinimo = i
        promedio += i

promedio /= len(listaNumeros)

print("El valor maximo de los numeros ingresados es: ",valorMaximo)
print("El valor minimo de los numeros ingresados es: ",valorMinimo)
print("El promedio de los numeros ingresados es: ",promedio)


    
        




