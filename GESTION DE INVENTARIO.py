import json

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self._id = id
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @property
    def cantidad(self):
        return self._cantidad

    @property
    def precio(self):
        return self._precio

    @cantidad.setter
    def cantidad(self, cantidad):
        self._cantidad = cantidad

    @precio.setter
    def precio(self, precio):
        self._precio = precio

    def __str__(self):
        return f"ID: {self._id}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: {self._precio}"

class Inventario:
    def __init__(self, archivo="inventario.json"):
        self.productos = {}
        self.archivo = archivo
        self.cargar_inventario()

    def agregar_producto(self, producto):
        if producto.id in self.productos:
            print(f"El producto con el ID {producto.id} ya existe.")
            return
        self.productos[producto.id] = producto
        self.guardar_inventario()
        print("Producto agregado exitosamente.")

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            self.guardar_inventario()
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id, **kwargs):
        if id in self.productos:
            producto = self.productos[id]
            for attr, value in kwargs.items():
                if hasattr(producto, attr):
                    setattr(producto, attr, value)
            self.guardar_inventario()
            print("Producto actualizado.")
        else:
            print("Producto no encontrado.")

    def buscar_productos(self, nombre):
        resultados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        if resultados:
            for producto in resultados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

    def guardar_inventario(self):
        with open(self.archivo, "w") as f:
            productos_serializados = {id: p.__dict__ for id, p in self.productos.items()}
            json.dump(productos_serializados, f, indent=4)

    def cargar_inventario(self):
        try:
            with open(self.archivo, "r") as f:
                productos_serializados = json.load(f)
                for id, datos_producto in productos_serializados.items():
                    self.productos[int(id)] = Producto(**datos_producto)
        except FileNotFoundError:
            print("Archivo de inventario no encontrado. Creando uno nuevo.")

if __name__ == "__main__":
    inventario = Inventario()

    while True:
        print("\nMenú:")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar productos")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            id = int(input("Ingrese el ID del producto: "))
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == 2:
            id = int(input("Ingrese el ID del producto a eliminar: "))
            inventario.eliminar_producto(id)
        elif opcion == 3:
            id = int(input("Ingrese el ID del producto a actualizar: "))
            nuevo_nombre = input("Nuevo nombre (deje en blanco si no desea cambiar): ")
            nueva_cantidad = input("Nueva cantidad (deje en blanco si no desea cambiar): ")
            nuevo_precio = input("Nuevo precio (deje en blanco si no desea cambiar): ")
            actualizaciones = {}
            if nuevo_nombre: actualizaciones["nombre"] = nuevo_nombre
            if nueva_cantidad: actualizaciones["cantidad"] = int(nueva_cantidad)
            if nuevo_precio: actualizaciones["precio"] = float(nuevo_precio)
            inventario.actualizar_producto(id, **actualizaciones)
        elif opcion == 4:
            nombre = input("Ingrese el nombre a buscar: ")
            inventario.buscar_productos(nombre)
        elif opcion == 5:
            inventario.mostrar_todos()
        elif opcion == 6:
            break
        else:
            print("Opción inválida.")