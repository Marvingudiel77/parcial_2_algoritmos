# plantear una funcion que reciba un string en mayusculas o minusculas y una letra
# luego el programa debe indicarle cuantas veces se encuentra la letra en el string
cadena_de_texto = input("Ingrese la cadena de texto deseada")
letra_repetida_min = "a"
letra_rep_may = "A"
contador_letra_min = 0
contador_letra_may = 0
for vocal in cadena_de_texto:
    if vocal == letra_repetida_min:
        contador_letra_min += 1

for vocal2 in cadena_de_texto:
    if vocal2 == letra_rep_may:
        contador_letra_may += 1

print(f"la letra {letra_repetida_min} se repite {contador_letra_min} de veces")
print(f"la letra {letra_rep_may} se repite {contador_letra_may} de veces")
