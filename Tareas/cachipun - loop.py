# ------------------------------
# ----- Cachipún
# ------------------------------

import sys
import random

while (True):
    print(" ")
    print("\t Bienvenido a ¡CA-CHI-PUN!")
    print("\t Para jugar, sólo debes escribir 'piedra', 'papel' o 'tijera'.")
    print("\t Para finalizar, debes escribir 'salir'.")
    print(" ")
    jugador = input("Tu jugada : ").lower()
    if (jugador == "piedra" or jugador == "papel" or jugador == "tijera"):
    # Variables
        jugadas = ["piedra", "papel", "tijera"]
        computador = random.choice(jugadas)
    # Posibilidades
    # 1 : Empate / 2 : Derrota / 3 : Victoria
        if (jugador == computador):
            resultado = 1
        elif ((jugador == "tijera" and computador == "piedra") or 
            (jugador == "papel" and computador == "tijera") or
            (jugador == "piedra" and computador == "papel")):
            resultado = 2
        else:
            resultado = 3
    # Inicio
        print(" ")
        print("\t ¡CA!")
        print("\t \t ¡CHI!")
        print("\t \t \t ¡PUN!")
        print(" ")
        print(f"[Sistema] : elegiste '{ jugador }'.")
        print(f"[Sistema] : tu oponente eligió '{ computador }'.")
    # Resultados
        print(" ")
        print("\t \t - [ R E S U L T A D O ] -")
        print(" ")
        if (resultado == 1):
            print(f"[Sistema] : Ambos eligieron '{ jugador }' ¡Empate!")
        if (resultado == 2):
            print(f"[Sistema] : ¡Perdiste! '{ jugador }' pierde contra '{ computador }'.")
        if (resultado == 3):
            print(f"[Sistema] : ¡Ganaste! '{ jugador }' le gana a '{ computador }'.")
        print(" ")
        print("¿Quieres jugar otra vez? ")
        encore = input("\t y/n : ").lower()
        if (encore == "y"):
            print(" ")
            print("---------------------")
            continue
        else:
            print(" ")
            print("[Sistema] : ¡Gracias por jugar!")
            sys.exit()
    elif (jugador == "salir"):
        print(" ")
        print("[Sistema] : ¡Gracias por jugar!")
        sys.exit()
    else:
        print(" ")
        print("---------- A D V E R T E N C I A")
        print(" ")
        print("[Sistema] : Sólo puedes utilizar las opciones 'piedra', 'papel' o 'tijera'.")
        print("[Sistema] : Para finalizar, utiliza 'salir'.")
