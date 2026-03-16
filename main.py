from menu import *

continuar=True
"""
errores a corregir=
1- si el segundo jugador pone una coordenada 
ya usada, la pisa - SOLUCIONADO
2- si se pone una coordenada mayor a la de la matriz se rompe- SOLUCIONADO
3- si gana el jugador 1 espera al segundo turno para comprobar-SOLUCIONADO
4- visualizar la coordenada-SOLUCIONADOS
5- visualizar dibujo-SOLUCIONADO
6-si hay empate no finaliza- SOLUCIONADO
"""
while continuar:
    vueltas=0
    jugando=True
    print(menu)
    decision=continuarMenu()
    if decision=="N":
        break
    else:
        matrisTateti= crearMatrizCeros()
        print(coordenadas)
        vueltas=0
    while jugando:
        print("Turno del Jugador 1 (x)")    
        cargarMatrizX(matrisTateti)
        mostrarmatriz(matrisTateti)
        vueltas+=1
        print("\n")
        #bandera3=comprobarGanador(matrisTateti)
        if comprobarGanador(matrisTateti):
            vueltas=0
            break
        if comprobarEmpate(matrisTateti,vueltas):
            vueltas=0
            break
        print("Turno del Jugador 2 (0)")    
        cargarMatriz0(matrisTateti)
        mostrarmatriz(matrisTateti)
        vueltas+=1
        print("\n")
        #bandera3=comprobarGanador(matrisTateti)
        if comprobarGanador(matrisTateti):
            vueltas=0
            break
        
            



