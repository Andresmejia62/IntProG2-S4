tiempo_lunes = float(input("Tiempo del lunes (minutos): "))
tiempo_miercoles = float(input("Tiempo del miércoles (minutos): "))
tiempo_viernes = float(input("Tiempo del viernes (minutos): "))

tiempo_promedio = (tiempo_lunes + tiempo_miercoles + tiempo_viernes) / 3

print(f"El tiempo promedio semanal es: {tiempo_promedio:.2f} minutos")
