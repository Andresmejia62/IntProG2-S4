#Diseña un algoritmo que intercambie el valor de dos variables numéricas. Usa una
#variable auxiliar para hacerlo.

a = 5
b = 10

print("Antes del intercambio: a =", a, "b =", b)

aux = a
a = b
b = aux

print("Después del intercambio: a =", a, "b =", b)