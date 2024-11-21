servidor = {"Juan1223":"J12an*." , "Maria2345":"M23a*.", "Pablo1459":"P14o*." , "Ana3456":"A34a*."}

intentosPermitidos = 3

while intentosPermitidos > 0:
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    
    if usuario in servidor:
        valor = servidor[usuario]
        if valor == contraseña:
            print("Acceso permitido")
            break

        else:
            intentosPermitidos -= 1
            print("Datos incorrectos")

    else:
        intentosPermitidos -= 1
        print("Datos incorrectos")

if intentosPermitidos == 0:
    print("Lo siento, su acceso no es permitido")





