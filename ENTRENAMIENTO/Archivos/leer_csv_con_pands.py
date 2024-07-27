import pandas as pd

#se usa la funcion read_csv para leer el archivo csv
df = pd.read_csv("archivos\\datos.csv")
df2 = pd.read_csv("archivos\\datos.csv")

#obteniendo los datos de la columna nombre
nombres = df["nombre"]

#slicing
#cadena = "0123456789"
#print(cadena[0:3])

#ordenando el dataframe por la edad 
df_ordenado = df.sort_values("edad")

#ordenandolo de forma descendente 
df_ordenado = df.sort_values("edad",ascending=False)

#concatenando los dos dataframes
df_concatenado = pd.concat([df,df2])

#accediendo a la primeras fila con head() de arriba para abajo
primeras_fila = df.head(2)

#accediendo a las ultimas filas con head() de abajo para arriba
ultimas_fila = df.tail(2)

#accediendo a la camtidad de filas y columnas con shape
filas_totales, columnas_totales = df.shape


#para obtener informacion de un csv cusamos el   .describe 
df_info = df.describe()

#accediendo a la edad de la fila 2
elemento_especifico_loc = df.loc[2,"edad"]

#accediendo a un elemento especifico del df con loc
elemento_especifico_loc = df.iloc[2,2]

#accediendo a todas los apellidos con loc
apellidos = df.loc[:,"apellido"]

#accediendo a todas los apellidos con iloc
apellidos = df.iloc[:,1]


#accediento a la fila 3 con loc
fila_3 = df.loc[2,:]

#accediento a la fila 3 con iloc
fila_3 = df.iloc[2,:]

#accediendo a filas con edad mayor que 30
mayor_que_30 = df.loc[df["edad"]>30,:]


print(mayor_que_30)