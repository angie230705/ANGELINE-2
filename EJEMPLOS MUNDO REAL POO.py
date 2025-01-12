class Libro:
    def __init__(self, titulo, autor, isbn, disponible):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print("El libro no está disponible.")

    def devolver(self):
        self.disponible = True
        print(f"El libro '{self.titulo}' ha sido devuelto.")

class Usuario:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        self.libros_prestados = []

    def prestar_libro(self, libro):
        if libro.disponible:
            self.libros_prestados.append(libro)
            libro.prestar()
            print(f"{self.nombre} ha prestado el libro '{libro.titulo}'.")
        else:
            print("El libro no está disponible.")

# Ejemplo de uso
libro1 = Libro("Don Quijote", "Miguel de Cervantes", "9788420635379", True)
usuario1 = Usuario("Juan Pérez", "12345678")

usuario1.prestar_libro(libro1)