texto = open("Laboratorio1/test_pr2.txt")
cadenaTexto = texto.read()
texto.close()
lista = cadenaTexto.split()
cantidad = 0
for i in lista:
    if "en" == i or "En" == i:
        cantidad+=1
print(cantidad)

