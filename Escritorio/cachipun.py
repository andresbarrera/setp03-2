def ganador_cachipun(conjunto_juego):
    if len(conjunto_juego) != 2:
        raise Exception ("Número incorrecto de participantes")
    juego_1=conjunto_juego[0]
    juego_2=conjunto_juego[1]
    if juego_1[1] != "p" and juego_1[1] != "r" and juego_1[1] != "t" and juego_2[1] != "p" and juego_2[1] != "r" and juego_2[1] != "t" :
        raise Exception ("Alguna jugada es incorrecta")
    if juego_1[1] == juego_2[1]:
        print("Gana",juego_1[0],"por empate")
    if juego_1[1] == "r" and juego_2[1] == "t":
        print("Gana",juego_1[0],"con piedra")
    if juego_1[1] == "r" and juego_2[1] == "p":
        print("Gana",juego_2[0],"con papel")
    if juego_1[1] == "p" and juego_2[1] == "r":
        print("Gana",juego_1[0],"con papel")
    if juego_1[1] == "p" and juego_2[1] == "t":
        print("Gana",juego_2[0],"con tijeras")
    if juego_1[1] == "t" and juego_2[1] == "p":
        print("Gana",juego_1[0],"con tijeras")
    if juego_1[1] == "t" and juego_2[1] == "r":
        print("Gana",juego_2[0],"con piedra")
