# SmartGastro - Motor Lógico

class Producto:
    def __init__(self, nombre, precio, stock_inicial):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock_inicial

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def get_stock(self):
        return self.__stock

    def set_stock(self, cantidad):
        if cantidad >= 0:
            self.__stock = cantidad
        else:
            print(f"\n[ERROR]: No se puede asignar un stock negativo a {self.__nombre}.")

    def __str__(self):
        return f"Producto: {self.__nombre:15} | Precio: ${self.__precio:<8} | Stock: {self.__stock}"


class Inventario:
    def __init__(self):
        self.__lista_productos = []

    def agregar_producto(self, producto):
        self.__lista_productos.append(producto)
        print(f"\n[SISTEMA]: {producto.get_nombre()} agregado al inventario.")

    def mostrar_inventario(self):
        print("\n--- INVENTARIO ACTUAL ---")
        if not self.__lista_productos:
            print("El inventario está vacío.")
        for p in self.__lista_productos:
            print(p)

    def buscar_producto(self, nombre):
        for p in self.__lista_productos:
            if p.get_nombre().lower() == nombre.lower():
                return p
        return None


def ejecutar_menu():
    mi_inventario = Inventario()

    while True:
        print("\n=== SISTEMA SMARTGASTRO ===")
        print("1. Agregar Producto")
        print("2. Registrar Venta")
        print("3. Mostrar Inventario")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio: "))
            stock = int(input("Stock inicial: "))
            nuevo_p = Producto(nombre, precio, stock)
            mi_inventario.agregar_producto(nuevo_p)

        elif opcion == "2":
            nombre_venta = input("¿Qué producto desea vender?: ")
            producto = mi_inventario.buscar_producto(nombre_venta)

            if producto:
                cantidad = int(input(f"¿Cuántas unidades de {producto.get_nombre()}?: "))
                stock_actual = producto.get_stock()

                # Validación de stock
                if stock_actual >= cantidad:
                    nuevo_stock = stock_actual - cantidad
                    producto.set_stock(nuevo_stock)
                    print(f"\n[VENTA]: {cantidad} x {producto.get_nombre()} registrada con éxito.")
                else:
                    print(f"\n[ERROR]: Stock insuficiente. Solo quedan {stock_actual} unidades.")
            else:
                print("\n[ERROR]: Producto no encontrado.")

        elif opcion == "3":
            mi_inventario.mostrar_inventario()

        elif opcion == "4":
            print("Cerrando SmartGastro... ¡Hasta luego!")
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    ejecutar_menu()
