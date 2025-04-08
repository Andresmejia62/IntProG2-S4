precio_1 = float(input("Precio del primer producto: "))
precio_2 = float(input("Precio del segundo producto: "))
precio_3 = float(input("Precio del tercer producto: "))

subtotal = precio_1 + precio_2 + precio_3
iva = subtotal * 0.15
total_a_pagar = subtotal + iva

print(f"Subtotal: ${subtotal:.2f}")
print(f"IVA (15%): ${iva:.2f}")
print(f"Total a pagar: ${total_a_pagar:.2f}")
