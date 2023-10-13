#Parte 3

from readchar import readkey, key 
import os
def borrar_pantalla():
    os.system('cls' if os.name=='nt' else 'clear')

def imprimir_numero(contador):
    print(contador)
numero=0
print("¡Hola, Jugador! Para jugar, presiona la tecla N")

while True:
    tecla = readkey()
    if tecla == "n":
        borrar_pantalla()
        imprimir_numero(numero)
        if numero==50:
            print("Llegaste a 50, el juego ha terminado :)")
            break    
        numero = numero + 1  
