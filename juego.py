#Parte 2

from readchar import readkey, key 

print("¡Hola, Jugador! Para jugar, presiona cualquier tecla")
print("Si deseas parar, presiona la techa hacia arriba (↑)")

while True:
    tecla = readkey()
    if tecla == key.UP:
        print ("Haz finalizado el juego")
        break
    print(f"Haz presionado la tecla: {tecla}")
