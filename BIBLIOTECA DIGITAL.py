class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (autor, titulo)  # Tupla inmutable con autor y título
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[1]} por {self.info[0]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros actualmente prestados

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}, Libros prestados: {len(self.libros_prestados)}"


class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario con ISBN como clave y Libro como valor
        self.usuarios_registrados = set()  # Conjunto de IDs de usuarios únicos
        self.prestamos = {}  # Diccionario con ID de usuario como clave y lista de libros prestados como valor

    def agregar_libro(self, libro):
        self.libros_disponibles[libro.isbn] = libro
        print(f"Libro añadido: {libro}")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            libro = self.libros_disponibles.pop(isbn)
            print(f"Libro eliminado: {libro}")
        else:
            print("El libro con este ISBN no existe en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios_registrados:
            self.usuarios_registrados.add(usuario.id_usuario)
            self.prestamos[usuario.id_usuario] = []
            print(f"Usuario registrado: {usuario}")
        else:
            print("El usuario ya está registrado.")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            if not self.prestamos[id_usuario]:
                self.usuarios_registrados.remove(id_usuario)
                del self.prestamos[id_usuario]
                print(f"Usuario con ID {id_usuario} dado de baja.")
            else:
                print("No se puede dar de baja al usuario, tiene libros prestados.")
        else:
            print("El usuario no está registrado.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios_registrados:
            print("El usuario no está registrado.")
            return
        if isbn not in self.libros_disponibles:
            print("El libro no está disponible.")
            return
        libro = self.libros_disponibles.pop(isbn)
        self.prestamos[id_usuario].append(libro)
        print(f"Libro prestado a {id_usuario}: {libro}")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.prestamos:
            for libro in self.prestamos[id_usuario]:
                if libro.isbn == isbn:
                    self.prestamos[id_usuario].remove(libro)
                    self.libros_disponibles[isbn] = libro
                    print(f"Libro devuelto por {id_usuario}: {libro}")
                    return
        print("El usuario no tiene prestado este libro.")

    def buscar_libro(self, criterio, valor):
        resultados = [libro for libro in self.libros_disponibles.values() if
                      valor.lower() in str(getattr(libro, criterio)).lower()]
        for libro in resultados:
            print(libro)
        if not resultados:
            print("No se encontraron libros.")

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.prestamos and self.prestamos[id_usuario]:
            print(f"Libros prestados a {id_usuario}:")
            for libro in self.prestamos[id_usuario]:
                print(libro)
        else:
            print("El usuario no tiene libros prestados.")


# Prueba del sistema
biblioteca = Biblioteca()

libro1 = Libro("1984", "George Orwell", "Ficción", "123456")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", "789012")
usuario1 = Usuario("Juan Pérez", "U001")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.registrar_usuario(usuario1)
biblioteca.prestar_libro("U001", "123456")
biblioteca.listar_libros_prestados("U001")
biblioteca.devolver_libro("U001", "123456")
biblioteca.buscar_libro("categoria", "Ficción")
