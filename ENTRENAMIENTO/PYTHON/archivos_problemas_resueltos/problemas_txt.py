#2 lostas, una con nombres y otra con apellidos
nombres = ["Lucas","Matias","camila","Pedro","Roberto"]
apellidos = ["Dalto","Zing","Alcaraz","robertix","Tarado"]

#registrar esta informacion en un TXT de forma optima

with open("nombres_y_apellidos.txt","w") as arch:
    arch.writelines("Los datos son:\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n----------\n") for n,a in zip(nombres,apellidos)]