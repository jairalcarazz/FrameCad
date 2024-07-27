cadena1 = "Hola,soy,Dalto"
cadena2 = "Que onda master"

#Convierte todo en mayuscula
mayusc = cadena1.upper()

#Convierte todo en minuscula
minusc = cadena1.lower()

#Primera letra Mayuscula
primer_letra_mayusc = cadena1.capitalize

#Buscamos una cadena en otra cadena
busqueda_find = cadena1.find("a")

#es numerico nos devuelve true si no false 
es_numerico = cadena1.isnumeric()

#si ses numerico se devuelve true, si no devolvemos false 
es_alfanumerico = cadena1.isalpha()

#contamos coincidencias de una cadena dentro de otra cadena, devuelve la cantidad de coincidencias
contar_coincidencias = cadena1.count("da")

#contamos cuantos caracteres, tiene una cadena
contar_caracteres = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve true
empieza_con = cadena1.startswith("H")

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve true
termina_con = cadena1.endswith("H")

#remplaza un pedazo de la cadena dada, por otra dada 
cadena_nueva = cadena1.replace(",", " ")

#separar cadenas con la cadena que le pasemos 
cadena_separada = cadena1.split(",")

print(cadena_nueva)