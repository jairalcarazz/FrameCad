#creando una funcion simple
def saludar():
    print("Hola che, masterpiece")
    
saludar()

#crear una funcion que tenga parametros
#parametro es algo que se usa solo para el momento

def saludar(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif(sexo == "hombre"):
        adjetivo = "titan"
    else:
        adjetivo = "amor"
        
    print(f"Hola {nombre}, mi {adjetivo} , Como vas?")
    
saludar("Camila","Mujer")
saludar("Dalto","hombre")
saludar("Fran","no binario")


#crear una funcion que nos retorne valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num 
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num_entero*2}"
    print(contraseña)
    
password = crear_contraseña_random(3)
frase = f"Tu nueva contraseña es: {password}"
print(frase)


 