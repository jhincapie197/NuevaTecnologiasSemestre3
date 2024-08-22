#Solicitar una contraseña, validar si esta tiene una longitud mayor o igual a 16, validar si la contraseña ingresada es igual a una propuesta por usted, si es igual debe mostrar contraseña correcta, 
#de lo contrario contraseña incorrecta. Debe tener en cuenta tambien la posibilidad que la contraseña no tenga la longitud requerida.
#Funcion para determinar la longitud: len(contraseña)


contrasena_propuesta = "Micontrasenasegura2024"
contrasena_ingresada = input("Por favor, ingresa la contraseña: ")

#Verificar la longitud de la contraseña
if len(contrasena_ingresada) >= 16:
        
    if contrasena_ingresada == contrasena_propuesta:
        print("Contraseña correcta.")
    else:
        print("Contraseña incorrecta.")
        
else:
    print("La contraseña debe tener al menos 16 caracteres.")

