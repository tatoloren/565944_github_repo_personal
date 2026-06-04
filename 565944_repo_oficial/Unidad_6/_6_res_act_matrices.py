# Generar la matriz de ventas
ventas = [
    [10, 12, 8, 9],   # Producto 1
    [5, 7, 6, 8],     # Producto 2
    [15, 14, 13, 16]  # Producto 3
]


# 1 Total vendido por producto, genera la lista venta_productos
venta_productos = []
for producto in ventas:
    venta_productos.append(sum(producto))


# 2 Total vendido por dia, generar la lista venta_diaria
venta_dias=[]
for i in range(len(ventas[0])):
    venta_dias.append(0)

# Iterar la matrix, por filas y por columnas, usando los indices para hacer el cálculo
for producto in ventas:
    for index_dia, venta in enumerate(producto):
        venta_dias[index_dia] += venta


print(f"\nVentas por productos: ")
for index_producto, venta_producto in enumerate(venta_productos):
    print(f"Producto {index_producto+1}: {venta_producto}")


print(f"\nVentas diarias: ")
for index_dia, venta_dia in enumerate(venta_dias):
    print(f"Día {index_dia+1}: {venta_dia}")


# 3 Producto más vendido
max_ventas = max(venta_productos)

numero_producto = 1
for venta_producto in venta_productos:
    if venta_producto == max_ventas:
        print("\nProducto más vendido: Producto", numero_producto)
        print("Cantidad vendida:", venta_producto)
    numero_producto += 1