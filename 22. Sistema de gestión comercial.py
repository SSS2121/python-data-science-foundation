"""
Sistema de Gestión Comercial
Gestiona productos, inventario, clientes y ventas con POO
"""

from datetime import datetime
from typing import List, Optional


class Producto:
    """Representa un producto en el inventario."""
    
    def __init__(self, id: int, nombre: str, precio: float, stock: int):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f} (Stock: {self.stock})"
    
    def __repr__(self):
        return f"Producto({self.id}, '{self.nombre}', {self.precio}, {self.stock})"
    
    def actualizar_stock(self, cantidad: int) -> bool:
        """Actualiza el stock del producto."""
        if self.stock + cantidad < 0:
            return False
        self.stock += cantidad
        return True
    
    def esta_disponible(self, cantidad: int = 1) -> bool:
        """Verifica si hay suficiente stock."""
        return self.stock >= cantidad


class Cliente:
    """Representa un cliente del sistema."""
    
    def __init__(self, id: int, nombre: str, email: str, telefono: str):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.fecha_registro = datetime.now()
    
    def __str__(self):
        return f"{self.nombre} ({self.email})"
    
    def __repr__(self):
        return f"Cliente({self.id}, '{self.nombre}', '{self.email}')"


class Venta:
    """Representa una venta realizada."""
    
    def __init__(self, id: int, cliente: Cliente):
        self.id = id
        self.cliente = cliente
        self.fecha = datetime.now()
        self.items = []  # Lista de (Producto, cantidad)
        self.total = 0.0
    
    def agregar_item(self, producto: Producto, cantidad: int) -> bool:
        """Agrega un producto a la venta."""
        if not producto.esta_disponible(cantidad):
            print(f"Error: Stock insuficiente de {producto.nombre}")
            return False
        
        self.items.append((producto, cantidad))
        self.total += producto.precio * cantidad
        producto.actualizar_stock(-cantidad)
        return True
    
    def calcular_total(self) -> float:
        """Calcula el total de la venta."""
        return self.total
    
    def aplicar_descuento(self, porcentaje: float) -> None:
        """Aplica descuento al total."""
        if 0 <= porcentaje <= 100:
            descuento = self.total * (porcentaje / 100)
            self.total -= descuento
    
    def __str__(self):
        items_info = "\n".join([f"  - {p.nombre}: {c} x ${p.precio:.2f}" 
                                for p, c in self.items])
        return f"Venta #{self.id}\nCliente: {self.cliente.nombre}\n{items_info}\nTotal: ${self.total:.2f}"


class Inventario:
    """Gestiona el inventario de productos."""
    
    def __init__(self):
        self.productos = {}  # id -> Producto
    
    def agregar_producto(self, producto: Producto) -> bool:
        """Agrega un producto al inventario."""
        if producto.id in self.productos:
            print(f"Error: El producto {producto.id} ya existe")
            return False
        self.productos[producto.id] = producto
        return True
    
    def obtener_producto(self, id: int) -> Optional[Producto]:
        """Obtiene un producto por ID."""
        return self.productos.get(id)
    
    def listar_productos(self) -> List[Producto]:
        """Lista todos los productos."""
        return list(self.productos.values())
    
    def buscar_por_nombre(self, nombre: str) -> List[Producto]:
        """Busca productos por nombre."""
        return [p for p in self.productos.values() 
                if nombre.lower() in p.nombre.lower()]
    
    def actualizar_precio(self, id: int, nuevo_precio: float) -> bool:
        """Actualiza el precio de un producto."""
        producto = self.obtener_producto(id)
        if producto:
            producto.precio = nuevo_precio
            return True
        return False
    
    def obtener_valor_total(self) -> float:
        """Calcula el valor total del inventario."""
        return sum(p.precio * p.stock for p in self.productos.values())


class GestorClientes:
    """Gestiona los clientes del sistema."""
    
    def __init__(self):
        self.clientes = {}  # id -> Cliente
    
    def agregar_cliente(self, cliente: Cliente) -> bool:
        """Agrega un cliente al sistema."""
        if cliente.id in self.clientes:
            print(f"Error: El cliente {cliente.id} ya existe")
            return False
        self.clientes[cliente.id] = cliente
        return True
    
    def obtener_cliente(self, id: int) -> Optional[Cliente]:
        """Obtiene un cliente por ID."""
        return self.clientes.get(id)
    
    def listar_clientes(self) -> List[Cliente]:
        """Lista todos los clientes."""
        return list(self.clientes.values())
    
    def buscar_por_nombre(self, nombre: str) -> List[Cliente]:
        """Busca clientes por nombre."""
        return [c for c in self.clientes.values() 
                if nombre.lower() in c.nombre.lower()]


class SistemaVentas:
    """Sistema principal de gestión comercial."""
    
    def __init__(self):
        self.inventario = Inventario()
        self.gestor_clientes = GestorClientes()
        self.ventas = {}  # id -> Venta
        self.siguiente_id_venta = 1
    
    def crear_venta(self, cliente_id: int) -> Optional[Venta]:
        """Crea una nueva venta."""
        cliente = self.gestor_clientes.obtener_cliente(cliente_id)
        if not cliente:
            print(f"Error: Cliente {cliente_id} no encontrado")
            return None
        
        venta = Venta(self.siguiente_id_venta, cliente)
        self.ventas[self.siguiente_id_venta] = venta
        self.siguiente_id_venta += 1
        return venta
    
    def completar_venta(self, venta_id: int) -> bool:
        """Completa una venta."""
        if venta_id not in self.ventas:
            print(f"Error: Venta {venta_id} no encontrada")
            return False
        
        venta = self.ventas[venta_id]
        print(f"Venta #{venta.id} completada - Total: ${venta.total:.2f}")
        return True
    
    def obtener_reporte_ventas(self) -> str:
        """Genera un reporte de ventas."""
        total_ventas = sum(v.total for v in self.ventas.values())
        cantidad_ventas = len(self.ventas)
        
        reporte = f"""
        ========== REPORTE DE VENTAS ==========
        Total de ventas: {cantidad_ventas}
        Ingresos totales: ${total_ventas:.2f}
        Promedio por venta: ${total_ventas / cantidad_ventas if cantidad_ventas > 0 else 0:.2f}
        =======================================
        """
        return reporte
    
    def obtener_reporte_inventario(self) -> str:
        """Genera un reporte del inventario."""
        reporte = "========== REPORTE DE INVENTARIO ==========\n"
        
        for producto in self.inventario.listar_productos():
            valor = producto.precio * producto.stock
            reporte += f"{producto.nombre}: {producto.stock} unidades - ${valor:.2f}\n"
        
        reporte += f"Valor total del inventario: ${self.inventario.obtener_valor_total():.2f}\n"
        reporte += "==========================================="
        return reporte


# Ejemplo de uso
if __name__ == "__main__":
    # Crear sistema
    sistema = SistemaVentas()
    
    # Agregar productos
    sistema.inventario.agregar_producto(Producto(1, "Laptop", 999.99, 5))
    sistema.inventario.agregar_producto(Producto(2, "Mouse", 25.50, 20))
    sistema.inventario.agregar_producto(Producto(3, "Teclado", 75.00, 15))
    
    # Agregar clientes
    sistema.gestor_clientes.agregar_cliente(Cliente(1, "Juan García", "juan@email.com", "123456789"))
    sistema.gestor_clientes.agregar_cliente(Cliente(2, "María López", "maria@email.com", "987654321"))
    
    # Realizar venta 1
    venta1 = sistema.crear_venta(1)
    venta1.agregar_item(sistema.inventario.obtener_producto(1), 1)  # 1 Laptop
    venta1.agregar_item(sistema.inventario.obtener_producto(2), 2)  # 2 Mouses
    venta1.aplicar_descuento(5)  # Descuento del 5%
    print(venta1)
    sistema.completar_venta(venta1.id)
    
    print("\n" + "="*50 + "\n")
    
    # Realizar venta 2
    venta2 = sistema.crear_venta(2)
    venta2.agregar_item(sistema.inventario.obtener_producto(3), 1)  # 1 Teclado
    venta2.agregar_item(sistema.inventario.obtener_producto(2), 1)  # 1 Mouse
    print(venta2)
    sistema.completar_venta(venta2.id)
    
    print("\n" + "="*50 + "\n")
    
    # Reportes
    print(sistema.obtener_reporte_ventas())
    print("\n" + sistema.obtener_reporte_inventario())
    
    # Búsquedas
    print("\n" + "="*50)
    print("BÚSQUEDAS:")
    print("Productos con 'o' en el nombre:", [p.nombre for p in sistema.inventario.buscar_por_nombre("o")])
    print("Clientes con 'García':", [c.nombre for c in sistema.gestor_clientes.buscar_por_nombre("García")])
