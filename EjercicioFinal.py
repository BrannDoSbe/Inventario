class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio
        self.__cantidad = cantidad

    #Getters Setters
    @property
    def nombre(self):
        return self.__nombre

    @property
    def categoria(self):
        return self.__categoria
    
    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, precio):
            self.__precio = precio

    @property
    def cantidad(self):
        return self.__cantidad
    
    @cantidad.setter
    def cantidad(self, cantidad):
        self.__cantidad = cantidad

         
    def actualizar(self, nuevo_precio=None, nueva_cantidad=None):
        if nuevo_precio is not None and nuevo_precio > 0:
            self.precio = nuevo_precio
        if nueva_cantidad is not None and nueva_cantidad >= 0:
            self.cantidad = nueva_cantidad

    def __str__(self):
        return f"Producto: {self.nombre}, Categoría: {self.categoria}, Precio: {self.precio}, Cantidad: {self.cantidad}"


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if not any(p.nombre == producto.nombre for p in self.productos):
            self.productos.append(producto)
            print(f"Producto '{producto.nombre}' agregado al inventario.")
        else:
            print(f"El producto '{producto.nombre}' ya existe en el inventario.")

    def actualizar_producto(self, nombre, precio=None, cantidad=None):
        for producto in self.productos:
            if producto.nombre == nombre:
                producto.actualizar(precio, cantidad)
                print(f"Producto '{nombre}' actualizado.")
                return
        print(f"Producto '{nombre}' no encontrado en el inventario.")

    def eliminar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                self.productos.remove(producto)
                print(f"Producto '{nombre}' eliminado del inventario.")
                return
        print(f"Producto '{nombre}' no encontrado en el inventario.")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("Inventario:")
            for producto in self.productos:
                print(producto)

    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                print(producto)
                return
        print(f"Producto '{nombre}' no encontrado en el inventario.")


# Funciones de entrada segura para validación
def ingresar_numero_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("El valor debe ser mayor que 0.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")

def ingresar_cantidad(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor >= 0:
                return valor
            else:
                print("La cantidad debe ser mayor o igual a 0.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")


# Función para mostrar el menú
def mostrar_menu():
    print("\n--- Menú de Inventario ---")
    print("1. Agregar producto")
    print("2. Actualizar producto")
    print("3. Eliminar producto")
    print("4. Buscar producto")
    print("5. Mostrar inventario")
    print("6. Salir")
    return input("Selecciona una opción: ")


# Ejemplo de uso con un menú
inventario = Inventario()

while True:
    opcion = mostrar_menu()

    if opcion == '1':
        # Agregar producto
        nombre = input("Nombre del producto: ")
        categoria = input("Categoría del producto: ")
        precio = ingresar_numero_positivo("Precio del producto: ")
        cantidad = ingresar_cantidad("Cantidad en stock: ")
        producto = Producto(nombre, categoria, precio, cantidad)
        inventario.agregar_producto(producto)

    elif opcion == '2':
        # Actualizar producto
        nombre_actualizar = input("Nombre del producto a actualizar: ")
        nuevo_precio = ingresar_numero_positivo("Nuevo precio (deja en blanco para no cambiar): ") if input("¿Quieres cambiar el precio? (s/n): ").lower() == 's' else None
        nueva_cantidad = ingresar_cantidad("Nueva cantidad (deja en blanco para no cambiar): ") if input("¿Quieres cambiar la cantidad? (s/n): ").lower() == 's' else None
        inventario.actualizar_producto(nombre_actualizar, nuevo_precio, nueva_cantidad)

    elif opcion == '3':
        # Eliminar producto
        nombre_eliminar = input("Nombre del producto a eliminar: ")
        inventario.eliminar_producto(nombre_eliminar)

    elif opcion == '4':
        # Buscar producto
        nombre_buscar = input("Nombre del producto a buscar: ")
        inventario.buscar_producto(nombre_buscar)

    elif opcion == '5':
        # Mostrar inventario
        inventario.mostrar_inventario()

    elif opcion == '6':
        # Salir del programa
        print("Saliendo del sistema de inventario...")
        break

    else:
        print("Opción no válida, por favor selecciona una opción del 1 al 6.")
