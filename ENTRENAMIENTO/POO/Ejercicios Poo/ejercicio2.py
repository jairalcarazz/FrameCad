class Animal:
    def comer(self):
        print("el animal come")
        
        
class Ave(Animal):
    def volar(self):
        print("el animal vuela")
        
class Mamifero:
    def amamantar(self):
        print("el animal amamanta")
        
class Murcielago(Mamifero,Ave):
    pass

murcielago = Murcielago()
    
murcielago.comer()
murcielago.amamantar()
murcielago.volar()
