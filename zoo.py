class Animal:
    def __init__(self, nombre, edad, nivel_salud, nivel_felicidad):
        self.nombre = nombre
        self.edad = edad
        self.nivel_salud = nivel_salud
        self.nivel_felicidad = nivel_felicidad

    def mostrar_info(self):
        print("Nombre:", self.nombre)
        print("Salud:", self.nivel_salud)
        print("Felicidad:", self.nivel_felicidad)

    def alimentar(self):
        self.nivel_salud += 10
        self.nivel_felicidad += 10


class Leon(Animal):
    def __init__(self, nombre, edad, nivel_salud, nivel_felicidad, melena):
        super().__init__(nombre, edad, nivel_salud, nivel_felicidad)
        self.melena = melena

    def rugir(self):
        print("¡Rugido del león!")


class Tigre(Animal):
    def __init__(self, nombre, edad, nivel_salud, nivel_felicidad, rayas):
        super().__init__(nombre, edad, nivel_salud, nivel_felicidad)
        self.rayas = rayas

    def cazar(self):
        print("El tigre está cazando...")


class Oso(Animal):
    def __init__(self, nombre, edad, nivel_salud, nivel_felicidad, color):
        super().__init__(nombre, edad, nivel_salud, nivel_felicidad)
        self.color = color

    def pescar(self):
        print("El oso está pescando...")

    def mostrar_info(self):
        super().mostrar_info()
        print("Color:", self.color)


class Zoo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.animales = []

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def mostrar_animales(self):
        print("Animales en el zoológico:")
        for animal in self.animales:
            animal.mostrar_info()


# Ejemplo de uso
zoo = Zoo("Mi Zoológico")

leon1 = Leon("Simba", 5, 80, 90, "Marrón")
tigre1 = Tigre("Shere Khan", 6, 70, 85, "Naranja y negro")
oso1 = Oso("Baloo", 8, 90, 95, "Negro")

zoo.agregar_animal(leon1)
zoo.agregar_animal(tigre1)
zoo.agregar_animal(oso1)

zoo.mostrar_animales()

oso1.pescar()
oso1.alimentar()

zoo.mostrar_animales()
