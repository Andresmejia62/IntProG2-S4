total_cuenta = float(input("Total de la cuenta: "))
porcentaje_propina = float(input("Porcentaje de propina (%): "))

propina = total_cuenta * (porcentaje_propina / 100)

print(f"Debes dejar de propina: ${propina:.2f}")
