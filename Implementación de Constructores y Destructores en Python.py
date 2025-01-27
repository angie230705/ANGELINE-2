class Perro:
    """Clase que representa a un perro."""

    def __init__(self, nombre, raza):
        """Constructor de la clase Perro.
        Inicializa los atributos nombre y raza del perro.

        Args:
            nombre (str): El nombre del perro.
            raza (str): La raza del perro.
        """
        self.nombre = nombre
        self.raza = raza
        print(f"¡Hola! Soy un perro y me llamo {self.nombre}.")

    def ladrar(self):
        print("¡Guau!")

    def __del__(self):
        """Destructor de la clase Perro.
        Imprime un mensaje de despedida cuando el objeto es destruido.
        """
        print(f"Adiós. Ha sido un placer conocerte. Soy {self.nombre}.")

# Crear un objeto Perro
mi_perro = Perro("Max", "Labrador")

# Llamar al método ladrar
mi_perro.ladrar()

# El objeto mi_perro es destruido al salir del bloque, activando el destructor