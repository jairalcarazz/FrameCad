#cambiar el tipo de dato de una columna
import pandas as pd
df = pd.read_csv("archivos_problemas_resueltos\\datos.csv")

#convertir a string los datos de una columna
df['edad'] = df['edad'].astype(str)

#mostrar el tipo de dato del primer elemento en la columna edad
#print(type(df['edad'[0]]))

#remplazando los datos "Dalto" por "Maestro"
df['apellido'.replace("dalto","maestro",inplace = True)]

#eliminando las filas con datos faltantes
df = df.dropna()

#eliminando las filas repetidas
df = df.dropduplicates()

#creando un csv con el dataframe resultante
df.to_csv("archivos_problemas_resueltos\\datos_limpios.csv")

print(df)