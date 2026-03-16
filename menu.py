import numpy as np
menu="""
********************Bienvenidos al Ta-Te-Ti********************
---------------------------------------------------------------
Si desea jugar una partida, ingrese S
Si desea salir del programa, ingrese N
---------------------------------------------------------------

"""
coordenadas="""
aqui le presentamos las cordenadas 
a seleccionar:
        
    0,0  |  0,1  |  0,2 
   ----------------------
    1,0  |  1,1  |  1,2
   ----------------------
    2,0  |  2,1  |  2,2    

"""

def continuarMenu():#me aseguro que ingresen "s" o "n"
    while True:
        seguir=input("Desea Jugar? S - N: ").upper()
        if seguir != "S" and seguir != "N":
            print("opcion incorrecta, reingrese nuevamente : ")
        else:
            break    
    return seguir        
    
"""def opcionIngresada():#con esta funcion me simplifico pedir al usuario un numero y retornarl
    while True:
        num=input("ingrese el numero desado: ")
        try:
            opcion=int(num)
            break
        except ValueError:
            print("ingrese una opcion correcta")
            continue
    return opcion"""#respaldo del original

def opcionIngresadaJuego():#con esta funcion me simplifico pedir al usuario un numero y retornarl
    while True:
        num=input("ingrese el numero desado: ")
        try:
            opcion=int(num)
            if 0 <= opcion <= 2:
                return opcion
            else:
                print("coloque un rango correcto (de 0 a 2)")
        except ValueError:
            print("ingrese una opcion correcta")

def crearMatrizCeros():#con ceros
    matriz = np.zeros((3,3))
    return matriz

def cargarMatrizX(matrizJuego):#cargo la matriz para la x 
    while True:
        print("cargue la primer coordenada")
        i=opcionIngresadaJuego()
        print("cargue la segunda coordenada")
        j=opcionIngresadaJuego()    
        if matrizJuego[i,j] != 0 :
            print(end="\n")
            print("posicion ocupada, elija otra")   
        else:
            matrizJuego[i,j] = 1
            return matrizJuego   

def cargarMatriz0(matrizJuego):#cargo la matriz para la 0
    while True:
        print("cargue la primer coordenada")
        i=opcionIngresadaJuego()
        print("cargue la segunda coordenada")
        j=opcionIngresadaJuego()    
        if matrizJuego[i,j] != 0 :
            print(end="\n")
            print("posicion ocupada, elija otra")   
        else:
            matrizJuego[i,j] = 2
            return matrizJuego
     

def mostrarmatriz(matrizJuego):#muestro la matriz 
    print("\nEstado actual del tablero:")
    print("    0     1     2")
    for i in range(3):
        print("  +-----+-----+-----+")
        print(i, end=" |")
        for j in range(3):
            if matrizJuego[i, j] == 1:
                print("  x  |", end="")
            elif matrizJuego[i, j] == 2:
                print("  o  |", end="")
            else:
                print("     |", end="")
        print()
    print("  +-----+-----+-----+")

def recorrerMatriz(matriz,n):#recorro la matriz comprobando igualdad en las posiciones ganadoras
    bandera=False
    if matriz[1,1]==n:
        if matriz[0,2]==n and matriz[2,0]==n:
            bandera=True
        elif matriz[0,1]==n and matriz[2,1]==n:  
            bandera=True  
        elif matriz[0,0]==n and matriz[2,2]==n:  
            bandera=True
        elif matriz[1,0]==n and matriz[1,2]==n:  
            bandera=True
    elif matriz[0,0]==n:
        if matriz[0,1]==n and matriz[0,2]==n:
            bandera=True  
        elif matriz[1,0]==n and matriz[2,0]==n:
            bandera=True 
    elif matriz[2,2]==n:
        if matriz[2,1]==n and matriz[2,0]==n:
            bandera=True  
        elif matriz[1,2]==n and matriz[0,2]==n:
            bandera=True   
    return bandera     

def comprobarGanador(matriz):#corroboro si ya hay algun ganador
    jugador1=recorrerMatriz(matriz,1)
    jugador2=recorrerMatriz(matriz,2)
    if jugador1==True:
        print("*******************************************************")
        print("*       Felicidades, gano el jugador 1                *")
        print("*******************************************************")
        return True
    elif jugador2==True:
        print("*******************************************************")
        print("*       Felicidades, gano el jugador 2!               *")
        print("*******************************************************")
        return True
    else:
        return False
    

def comprobarEmpate(matriz,a):
    empate=comprobarGanador(matriz)
    contador=a
    if contador==9 and empate==False:
        print("*******************************************************")
        print("*          los jugadores han empatedo                 *")
        print("*******************************************************")
        return True

