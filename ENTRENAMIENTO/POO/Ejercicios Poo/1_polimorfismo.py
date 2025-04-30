class Gato():
    def sonido(self):
        return "Miau"
    
class Perro():
    def sonido(self):
        return "Guau"
    

gato = Gato()
perro = Perro()

print(perro.sonido())