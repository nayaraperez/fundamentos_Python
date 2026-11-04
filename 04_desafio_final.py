
nombre_producto =(input("Ingresa producto: "))
precio_unitario = int(input("Precio unitario: "))
cantidad = int(input("cantidad de productos: "))
disponible = True
dinero_cliente = int(input("cantidad de dinero del cliente: "))

subtotal = precio_unitario * cantidad
descuento = subtotal * 0.10
total_pagar = subtotal - descuento
dinero_restante = dinero_cliente - total_pagar

print(f'''
Producto: {nombre_producto} 
Precio unitario: ${precio_unitario}
Cantidad: {cantidad}
Disponible: {disponible}
''')

print(f'''
valor total sin descuento = ${subtotal}
Descuento del 10% = ${descuento}
Total a pagar = ${total_pagar}
Dinero restante = ${dinero_restante}
''')

print("Tipos de variables:")
print(type(nombre_producto))
print(type(precio_unitario))
print(type(cantidad))
print(type(disponible))
print(type(dinero_cliente))