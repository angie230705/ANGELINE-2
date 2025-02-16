class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if any(p.id == producto.id for p in self.productos):
            print("El producto con el ID", producto.id, "ya existe.")
            return
        self.productos.append(producto)
        print("Producto agregado exitosamente.")

    def eliminar_producto(self, id):
        for i, producto in enumerate(self.productos):
            if producto.id == id:
                del self.productos[i]
                print("Producto eliminado.")
                return
        print("Producto no encontrado.")

    def actualizar_producto(self, id, **kwargs):
        for producto in self.productos:
            if producto.id == id:
                for attr, value in kwargs.items():
                    setattr(producto, attr, value)
                print("Producto actualizado.")
                return
        print("Producto no encontrado.")

    def buscar_productos(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        if resultados:
            for producto in resultados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        if self.productos:
            for producto in self.productos:
                print(producto)
        else:
            print("El inventario está vacío.")

if __name__ == "__main__":
    inventario = Inventario()

    while True:
        print("\nMenú:")
        print("1. Manzana")
        print("2. Embutidos")
        print("3. carnes")
        print("4. Peras")
        print("5. Pollo")
        print("6. Atun")

        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            id = int(input("220055: "))
            nombre = input("Manzana: ")
            cantidad = int(input("1: "))
            precio = float(input("0.25: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == 2:
            id = int(input("220055: "))
            inventario.eliminar_producto(id)
        elif opcion == 3:
            id = int(input("220055: "))
            nuevo_nombre = input("Fruta: ")
            nueva_cantidad = input("5: ")
            nuevo_precio = input("0.50: ")
            inventario.actualizar_producto(id, nombre=nuevo_nombre, cantidad=nueva_cantidad, precio=nuevo_precio)
        elif opcion == 4:
            nombre = input("Ingrese el nombre a buscar: ")
            inventario.buscar_productos(nombre)
        elif opcion == 5:
            inventario.mostrar_todos()
        elif opcion == 6:
            break
        else:
            print("Opción inválida.")




