#para localizar archivos colocamos: archivos\\
#with open("archivos\\datos.csv"):
 #   print ("data leida correctamente")
#
  #  with open("archivos\\datos.csv"):
   # print ("data leida correctamente")
    
    
#csv es algo que tiene por default python 
import csv

with open("archivos\\datos.csv") as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)