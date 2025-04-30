#le pedimos al usuario que nos diga una frase
frase = input("decime una frase y te calculo cuanto tardarias si tuvieras que decirla: ")

#creamos una lista con todas las palabras de la frase (se separancada vez que haya un espacio en blanco)
palabras_separadas = frase.split(" ")

#usamos len() para ver la cantidad de elementos que hay en la lista
cantidad_de_palabras = len(palabras_separadas)

#en caso de que tarde mas de un minutoen decirlo le decimos que pare un poco
if cantidad_de_palabras > 120:
    print("Para flaco tampoco te pedi un testamento")

#Calculamos cuanto tardaria en decir las palabras y se lo decimos
print(f'Dijiste {cantidad_de_palabras}palabras y tardarias ')

