#creando una lista con list 
lista = list(["hola", "como", "estamos",34,56,23,True])

#devuelve la cantidad de elementos en una lista
cantidad_elementos = len(lista)

#agregabdo un elemento a la lista 
lista.append("jajaja")

#agregando un elemento a la lista en un indice especifico
lista.insert(2, "jalaaaaala")

#Agregando varios elementos a la lista 
lista.extend([False,2030])

#Eliminando un elemento (por su indice) -1 para eliminar el ultimo -2 para eliminar el penultimo y asi consecusivamente
lista.pop(-1)

#remover un elemento por el valor, es decir por lo que dice 
lista.remove(56)
 
 
#Elimina todos los elementos de la lista
#lista.clear()

#ordenando la lista de forma ascendente (si se usa el reverse=true se ordena en reversa)
lista.sort()

#inivirtiendo los elementos de una lista
lista.reverse()

print(lista)

