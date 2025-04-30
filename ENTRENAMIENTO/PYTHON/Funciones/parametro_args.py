#forma no optica de sumar valores
#def suma(lista):
#    numeros_sumados = 0
#    for numero in lista:
#       numeros_sumados = numeros_sumados + numero
#  return numeros_sumados

#resultado = suma({5,3,9,10,20,3})
#forma optima de sumar valores
def suma_total(numeros):
   return sum({*numeros})

resultado2 = suma_total([5,3,9,10,20,3])


#Utilizando el operador args como argumento y para desglosarrube
def suma(nombre,*numeros):
   return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"
    
resultado = suma("Lucas",5,3,9,10,20,3)
print(resultado)

