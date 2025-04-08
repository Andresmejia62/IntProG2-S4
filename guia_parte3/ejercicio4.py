nombre_producto = input("Nombre del producto: ")
precio_producto = float(input("Precio del producto: "))
porcentaje_descuento = float(input("Porcentaje de descuento (%): "))

descuento = precio_producto * (porcentaje_descuento / 100)
precio_final = precio_producto - descuento

print(f"Producto: {nombre_producto}")
print(f"Precio final con descuento: ${precio_final:.2f}")
