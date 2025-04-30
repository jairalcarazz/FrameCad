import re

texto = """Hola maestro como estas mi capitan
Esta es ka segunda linea
Y esta es la final mi capitan"""

#haciendo una busqueda simple
#resultado = re.findall("Esta", texto )

# \d -> busca digitos numericos de 0-9
#resultado = re.findall(r"\d",texto)

# \D -> busca TODO MENOS digitos numericos de 0-9
#resultado = re.findall(r"\D",texto)

# \w -> busca caracteres alfanumericos [a-z A-Z 0-9]
#resultado = re.findall(r"\w",texto)

# \W -> busca TODO MENOS caracteres alfanumericos [a-z A-Z 0-9]
#resultado = re.findall(r"\W",texto)

# \s -> busca espacios en blanco [espacios tab y saltos de linea]
#resultado = re.findall(r"\s",texto)

# \S -> busca TODO MENOS espacios en blanco [espacios tab y saltos de linea]
#resultado = re.findall(r"\S",texto)

# \r -> busca TODO MENOS saltos de linea]
#resultado = re.findall(r"\r",texto)

# \n -> busca saltos en linea
#resultado = re.findall(r'\n', texto)

# \ -> cancelar caracteres especiales , cancelando la funcion del punto y buscando puntos
#resultado = re.findall(r'\.',texto)

#armando una cadena que busque un numero seguido de un punto yb un espacio
#resultado = re.findall(f'\d\.\s',texto)

#Buscando el principio de una linea'
# ^ ->bueca el comienzo de una linea (buscando)
#resultado = re.findall(f'^Esta',texto,flags=re.IGNORECASE)
#resultado = re.findall(f'^Esta',texto,flags=re.M )
#flags=re.M activa la multilinea
 
 
 
#Buscando al final de una linea'
# $ ->bueca el final de una linea (buscando)
#resultado = re.findall(f'capitan$',texto,flags=re.IGNORECASE)

# {n} -> Busca n cantidad de veces el valor de la izquierda
#resultado = re.findalla(r'\d{3}',texto)

#{n,m} -> al menos n, como maximo m
#resultado = re.findall(r'\d{2,4}|Hola',texto)


#print(resultado)