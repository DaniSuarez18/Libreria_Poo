class Animal:
    def __init__(self,nombre):
        self.nombre = nombre 
       
    def sonido(self):
        return "hace un sonido"

class Perro(Animal):
    def sonido(self):
        return "hace GUAUU"   

class Gato(Animal):
    def sonido(self):
        return "hace MIAUU"  

class Lorito(Animal):
    def sonido(self):
        return "quiere CACAOO"

def crear_animal(tipo, nombre):
    tipos_animales = {
        "perro" : Perro,
        "gato" : Gato,
        "lorito" : Lorito
    }
    return tipos_animales.get(tipo.lower(), Animal)(nombre)

