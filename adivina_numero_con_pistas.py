import random

# Generar un número aleatorio entre 1 y 100
numero_aleatorio = random.randint(1, 100)

# Inicializar la adivinanza del usuario
adivinanza = None

# Continuar solicitando adivinanzas hasta que el usuario adivine correctamente
while adivinanza != numero_aleatorio:
    adivinanza = int(input("Adivina el número (entre 1 y 100): "))
    
    if adivinanza < numero_aleatorio:
        print("El número es mayor.")
    elif adivinanza > numero_aleatorio:
        print("El número es menor.")
    else:
        print("¡Felicidades! Adivinaste el número.")