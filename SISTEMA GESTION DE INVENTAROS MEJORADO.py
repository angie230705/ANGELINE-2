import os

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga el inventario desde un archivo si existe."""
        if not os.path.exists(self.archivo):
            print("Archivo de inventario no encontrado. Se creará uno nuevo.")
            return
        try:
            with open(self.archivo, "r") as file:
                for linea in file:
                    try:
                        id_producto, nombre, cantidad = linea.strip().split(",")
                        self.productos[id_producto] = {"nombre": nombre, "cantidad": int(cantidad)}
                    except ValueError:
                        print(f"Error al procesar línea: {linea}")
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error al abrir el archivo: {e}")

    def guardar_inventario(self):
        """Guarda el inventario actual en un archivo."""
        try:
            with open(self.archivo, "w") as file:
                for id_producto, datos in self.productos.items():
                    file.write(f"{id_producto},{datos['nombre']},{datos['cantidad']}\n")
            print("Inventario guardado exitosamente.")
        except (PermissionError, IOError) as e:
            print(f"Error al escribir en el archivo: {e}")

    def agregar_producto(self, id_producto, nombre, cantidad):
        """Agrega un nuevo producto al inventario."""
        if id_producto in self.productos:
            print("Error: Producto ya existente.")
            return
        self.productos[id_producto] = {"nombre": nombre, "cantidad": cantidad}
        self.guardar_inventario()
        print("Producto agregado exitosamente.")

    def actualizar_producto(self, id_producto, cantidad):
        """Actualiza la cantidad de un producto en el inventario."""
        if id_producto not in self.productos:
            print("Error: Producto no encontrado.")
            return
        self.productos[id_producto]["cantidad"] = cantidad
        self.guardar_inventario()
        print("Producto actualizado exitosamente.")

    def eliminar_producto(self, id_producto):
        """Elimina un producto del inventario."""
        if id_producto not in self.productos:
            print("Error: Producto no encontrado.")
            return
        del self.productos[id_producto]
        self.guardar_inventario()
        print("Producto eliminado exitosamente.")

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("El inventario está vacío.")
            return
        for id_producto, datos in self.productos.items():
            print(f"ID: {id_producto}, Nombre: {datos['nombre']}, Cantidad: {datos['cantidad']}")

# Programa principal
def menu():
    inventario = Inventario()
    while True:
        print("\n--- Sistema de Gestión de Inventarios ---")
        print("1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            try:
                cantidad = int(input("Ingrese cantidad: "))
                inventario.agregar_producto(id_producto, nombre, cantidad)
            except ValueError:
                print("Error: La cantidad debe ser un número entero.")

        elif opcion == "2":
            id_producto = input("Ingrese ID del producto: ")
            try:
                cantidad = int(input("Ingrese nueva cantidad: "))
                inventario.actualizar_producto(id_producto, cantidad)
            except ValueError:
                print("Error: La cantidad debe ser un número entero.")

        elif opcion == "3":
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "4":
            inventario.mostrar_inventario()

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    menu()
