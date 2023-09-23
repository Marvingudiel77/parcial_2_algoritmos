# Desarrollar un programa que por lineas de comandos debe recibir N cantidad de valores
# separados por comas y el programa debe devolver la suma y el promedio de todo el
# conjunto, tanto la suma y el promedio deben estar escritos como funciones

def Suma_y_promedio(lista):
    suma = sum(lista)
    promedio = suma / len(lista)
    return suma, promedio


def main():
    entrada = input(
        "ingrese los numeros deseados para su suma y promedio separados por espacios: ")
    numeros = [int(numero) for numero in entrada.split()]

    if len(numeros) == 0:
        print("La lista no contiene nada.")
    else:
        suma, promedio = Suma_y_promedio(numeros)
        print(f"Suma: {suma}")
        print(f"Promedio: {promedio}")


if __name__ == "__main__":
    main()
