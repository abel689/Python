class Ninja:
    def __init__(self, nombre, apellido, mascotas, premio, comida_mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.mascotas = mascotas
        self.premio = premio
        self.comida_mascota = comida_mascota

    def caminar(self):
        print(f"{self.nombre} {self.apellido} está caminando.")

    def alimentar(self):
        print(f"{self.nombre} {self.apellido} está alimentando a sus mascotas.")
        for mascota in self.mascotas:
            mascota.comer(self.comida_mascota)

    def bañar(self):
        print(f"{self.nombre} {self.apellido} está bañando a sus mascotas.")
        for mascota in self.mascotas:
            mascota.dormir()
            mascota.comer("golosinas")
            mascota.jugar()

class Mascota:
    def __init__(self, name, tipo, golosinas, salud, energía):
        self.name = name
        self.tipo = tipo
        self.golosinas = golosinas
        self.salud = salud
        self.energía = energía

    def dormir(self):
        print(f"{self.name} está durmiendo.")

    def comer(self, comida):
        print(f"{self.name} está comiendo {comida}.")
        self.salud += 10

    def jugar(self):
        print(f"{self.name} está jugando.")
        self.energía -= 10

    def sonido(self):
        if self.tipo == "perro":
            print(f"{self.name} hace '¡Guau!'")
        elif self.tipo == "gato":
            print(f"{self.name} hace '¡Miau!'")
        else:
            print(f"{self.name} hace un sonido desconocido.")

# Crear objetos Ninja y Mascota
ninja = Ninja("Naruto", "Uzumaki", [], "Medalla de Honor", "ramen")
mascota1 = Mascota("Kurama", "perro", 5, 50, 50)

# Agregar mascotas al ninja
ninja.mascotas.append(mascota1)
ninja.mascotas.append(mascota2)

# Llamar a los métodos de Ninja
ninja.caminar()
ninja.alimentar()
ninja.bañar()

# Llamar a los métodos de Mascota
mascota1.sonido()
