# ------------------------------
# ----- Cachipún
# ------------------------------

# ¿Son necesarios?
import sys
import random
# Check para ambas posibilidades
if (sys.argv[1] == "piedra" or sys.argv[1] == "papel" or sys.argv[1] == "tijera"):
# Variables
    jugadas = ["piedra", "papel", "tijera"]
    jugador = sys.argv[1]
    computador = random.choice(jugadas)
# Posibilidades
# 1 : Empate / 2 : Derrota / 3 : Victoria
    if (jugador == computador):
        resultado = 1
    if (jugador == "tijera" and computador == "piedra"):
        resultado = 2
    if (jugador == "papel" and computador == "tijera"):
        resultado = 2
    if (jugador == "piedra" and computador == "papel"):
        resultado = 2
    if (jugador == "tijera" and computador == "papel"):
        resultado = 3
    if (jugador == "papel" and computador == "piedra"):
        resultado = 3
    if (jugador == "piedra" and computador == "tijera"):
        resultado = 3
    print(" ")
    print("\t ¡CA!")
    print("\t \t ¡CHI!")
    print("\t \t \t ¡PUN!")
    print(" ")
    print(f"[Sistema] : elegiste { jugador }.")
    print(f"[Sistema] : tu oponente eligió { computador }.")
    print(" ")
    print("\t \t - [ R E S U L T A D O ] -")
    print(" ")
    if (resultado == 1):
        print(f"[Sistema] : Ambos eligieron { jugador } ¡Empate!")
    if (resultado == 2):
        print(f"[Sistema] : ¡Perdiste! { jugador } pierde contra { computador }.")
    if (resultado == 3):
        print(f"[Sistema] : ¡Ganaste! { jugador } le gana a { computador }.")
    print("[Sistema] : ¡Gracias por jugar!")
    sys.exit()
else:
    print(" ")
    print("---------- A D V E R T E N C I A")
    print(" ")
    print("[Sistema] : Sólo puedes utilizar las opciones < piedra >, < papel > o < tijera >.")
    sys.exit()
