class Animal:
    """Clase base que representa a un animal"""

    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Encapsulación
        self.__edad = edad

    def comer(self):
        print(f"{self.__nombre} está comiendo.")

    def hacer_sonido(self):
        print("El animal hace un sonido.")

class Perro(Animal):
    """Clase derivada que representa a un perro"""

    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def hacer_sonido(self):  # Sobrescritura de método
        print("¡Guau!")

    def jugar(self):
        print(f"{self.__nombre} está jugando a traer la pelota.")

class Gato(Animal):
    """Clase derivada que representa a un gato"""

    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color

    def hacer_sonido(self):
        print("¡Miau!")

    def dormir(self):
        print(f"{self.__nombre} está durmiendo.")

# Crear instancias de las clases
perro = Perro("Firulais", 3, "Labrador")
gato = Gato("Michi", 2, "Gris")

# Demostrar polimorfismo
def alimentar_animal(animal):
    animal.comer()
    animal.hacer_sonido()

# Uso de las clases y polimorfismo
alimentar_animal(perro)
alimentar_animal(gato)

# Demostrando encapsulación
# print(perro.__nombre)  # Esto daría error, ya que __nombre es privado
print(perro.nombre)  # Intentando acceder al atributo privado (no funcionará)

# Agregando más funcionalidades
def mostrar_info_animal(animal):
    print(f"Nombre: {animal.__nombre}")  # Acceso directo al atributo privado (no recomendado)
    print(f"Edad: {animal.__edad}")
    if isinstance(animal, Perro):
        print(f"Raza: {animal.raza}")
    elif isinstance(animal, Gato):
        print(f"Color: {animal.color}")

mostrar_info_animal(perro)
mostrar_info_animal(gato)