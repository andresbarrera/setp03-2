from random import * #esto permite ocupar el comando randint que genera numeros en un ciertor rango
def resultados_craps(condiciones):
    jugando = True #variable bandera para salir cuando se cumplen las condiciones de un ciclo
    primer_juego = (randint(1,6), randint(1,6))
    print("Este es el primer lanzamiento:" + str(primer_juego))
    if primer_juego in condiciones['victoria']:
        print("Usted ha ganado la partida de craps.")
    elif primer_juego in condiciones['derrota']:
        print("Usted ha perdido la partida de craps.")
    elif primer_juego in condiciones['punto']:
        primera_puntuacion = primer_juego[0] + primer_juego[1]
        while jugando:
            segundo_juego = (randint(1,6),randint(1,6))
            segunda_puntuacion = segundo_juego[0] + segundo_juego[1]
            print("Lanze nuevamente por favor")
            print("Usted tiró: " + str(segundo_juego))
            if segunda_puntuacion == 7:
                print("Usted ha perdido la partida de craps.")
                jugando = False
            elif segunda_puntuacion == primera_puntuacion:
                print("Usted ha ganado la partida de craps.")
                jugando = False
#Resultados_craps indica los resultados del juego

def craps():
    dado = []
    for i in range(13): #el largo de la lista llega a 13
        dado.append(set()) #se genera la lista con sets vacíos 
    for j in range(6):
        for k in range(6):#el largo de la lista llega a 6
            dado[j+k+2].add((j+1,k+1)) #se genera el conjunto de los juegos (considerando sumas)
    derrota = dado[2]|dado[3]|dado[12]
    victoria = dado[7]|dado[11]
    punto = dado[4]|dado[5]|dado[6]|dado[8]|dado[9]|dado[10]
    condiciones = {"derrota":derrota, "victoria":victoria, "punto": punto}	
    resultados_craps(condiciones)												   
#Craps ejecuta el programa en su totalidad
