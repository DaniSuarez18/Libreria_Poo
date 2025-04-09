from herencia_animales import crear_animal
from lista_animales import Zoo

def main():
    zoo = zoo()
    print("Bienvenido a sistema de animales: ")

    while True:
        nombre = input("ingrese el nombre de animal:")
        if nombre.lower() == "salir":
            break

        tipo = input("ingrese el tipo de animal(Perro, Gato, Lorito): ")
        animal = crear_animal(tipo, nombre)
        zoo.agregar_animal(animal)
        print(f"{animal.nombre} : {animal.sonido()}\n")

    print("\nLista de animales en el zoologico:")
    zoo.mostrar_animales()

main()