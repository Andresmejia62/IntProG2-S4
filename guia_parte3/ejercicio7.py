nota_tareas = float(input("Nota de tareas (sobre 100): "))
nota_parcial = float(input("Nota del examen parcial (sobre 100): "))
nota_final = float(input("Nota del examen final (sobre 100): "))

calificacion_final = (nota_tareas * 0.30) + (nota_parcial * 0.30) + (nota_final * 0.40)

print(f"Calificación final del estudiante: {calificacion_final:.2f}")
