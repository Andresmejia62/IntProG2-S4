#Crea un algoritmo que, dado el año de nacimiento de una persona y el año actual,
#calcule su edad actual y su edad en 10 años

anio_nacimiento = int(input("Ingresa tu año de nacimiento: "))
anio_actual = int(input("Ingresa el año actual: "))
edad_actual = anio_actual - anio_nacimiento
edad_en_10_anios = edad_actual + 10

print(f"Tu edad actual es: {edad_actual} años.")
print(f"Tu edad en 10 años será: {edad_en_10_anios} años.")