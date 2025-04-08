presupuesto_anual = float(input("Ingrese el presupuesto anual del hospital: "))

presupuesto_urgencias = presupuesto_anual * 0.37
presupuesto_pediatria = presupuesto_anual * 0.42
presupuesto_traumatologia = presupuesto_anual * 0.21

print(f"Presupuesto para Urgencias: ${presupuesto_urgencias:.2f}")
print(f"Presupuesto para Pediatría: ${presupuesto_pediatria:.2f}")
print(f"Presupuesto para Traumatología: ${presupuesto_traumatologia:.2f}")
