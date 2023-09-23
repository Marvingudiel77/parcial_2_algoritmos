# correccion del programa
mail = input("Ingrese un email: ")
cantidad = 0
x = 0

while x < len(mail):
    if mail[x] == "@":
        cantidad = cantidad + 1
    x = x + 1

if cantidad == 1:
    print("El email ingresado contiene solo un carácter @.")
else:
    print("El email ingresado es incorrecto, intente otra vez .")
