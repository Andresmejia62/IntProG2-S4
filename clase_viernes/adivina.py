#adivina un numero
import random

numero_secreto = random.randint(1, 10)

while(True):
    numero_usuario = int(input("Adivina el número entre 1 y 10: "))
    print("El número secreto es:", numero_secreto)
    if numero_usuario == numero_secreto:
        print("¡Felicidades! Adivinaste el número.")    
        break
    else:
        print("Lo siento, no adivinaste el número.")
        print("Intenta nuevamente.")

    if numero_usuario < numero_secreto:
        print("El número secreto es mayor.")      
    else:
        print("El número secreto es menor.")
