import numpy as np
import random
def mostrar_cubo():
    print("               ", blanco_superior[0])
    print("               ", blanco_superior[1])
    print("               ", blanco_superior[2])
    print(amarillo_inferior[0], verde_frontal[0], rojo_lateral_derecho[0], azul_lateral_izquierdo[0])
    print(amarillo_inferior[1], verde_frontal[1], rojo_lateral_derecho[1], azul_lateral_izquierdo[1])
    print(amarillo_inferior[2], verde_frontal[2], rojo_lateral_derecho[2], azul_lateral_izquierdo[2])


def rotar_antihorario(frontal, superior, lateral_derecho, inferior, lateral_izquierdo):
    # Rotar la matriz verde_frontal en sentido contrario a las manecillas del reloj
    frontal[:] = np.rot90(frontal, k=1)
    # Rotar las filas y columnas de las otras matrices
    fila_temp = superior[2].copy()
    superior[2][0] = lateral_derecho[0][0]
    superior[2][1] = lateral_derecho[1][0]
    superior[2][2] = lateral_derecho[2][0]
    lateral_derecho[0][0] = inferior[0][2]
    lateral_derecho[1][0] = inferior[0][1]
    lateral_derecho[2][0] = inferior[0][0]
    inferior[0][0] = lateral_izquierdo[2][2]
    inferior[0][1] = lateral_izquierdo[1][2]
    inferior[0][2] = lateral_izquierdo[0][2]
    lateral_izquierdo[0][2] = fila_temp[2]
    lateral_izquierdo[1][2] = fila_temp[1]
    lateral_izquierdo[2][2] = fila_temp[0]


def rotar_horario(frontal, superior, lateral_derecho, inferior, lateral_izquierdo):

    # Rotar la matriz verde_frontal en sentido de las manecillas del reloj
    frontal[:] = np.rot90(frontal, k=-1)
    # Rotar las filas y columnas de las otras matrices
    fila_temp = superior[2].copy()
    superior[2][0] = lateral_izquierdo[2][2]
    superior[2][1] = lateral_izquierdo[1][2]
    superior[2][2] = lateral_izquierdo[0][2]
    lateral_izquierdo[0][2] = inferior[0][0]
    lateral_izquierdo[1][2] = inferior[0][1]
    lateral_izquierdo[2][2] = inferior[0][2]
    inferior[0][0] = lateral_derecho[2][0]
    inferior[0][1] = lateral_derecho[1][0]
    inferior[0][2] = lateral_derecho[0][0]
    lateral_derecho[0][0] = fila_temp[0]
    lateral_derecho[1][0] = fila_temp[1]
    lateral_derecho[2][0] = fila_temp[2]


def frontal():
    print("Movimiento frontal")
    rotar_horario(verde_frontal, blanco_superior,
              rojo_lateral_derecho, amarillo_inferior, naranja_posterior)
    mostrar_cubo()

def frontal_primo():
    print("Movimiento frontal'")
    rotar_antihorario(verde_frontal, blanco_superior,
                  rojo_lateral_derecho, amarillo_inferior, naranja_posterior)
    mostrar_cubo()

def lateral_derecho():
    print("Movimiento lateral derecho")
    rotar_horario(rojo_lateral_derecho, blanco_superior,
              azul_lateral_izquierdo, amarillo_inferior, verde_frontal)
    mostrar_cubo()

def lateral_derecho_primo():
    print("Movimiento lateral derecho'")
    rotar_antihorario(rojo_lateral_derecho, blanco_superior,
                  azul_lateral_izquierdo, amarillo_inferior, verde_frontal)
    mostrar_cubo()

def superior():
    print("Movimiento superior")
    rotar_horario(blanco_superior, azul_lateral_izquierdo,
              rojo_lateral_derecho, verde_frontal, amarillo_inferior)
    mostrar_cubo()

def superior_primo():
    print("Movimiento superior'")
    rotar_antihorario(blanco_superior, azul_lateral_izquierdo,
                  rojo_lateral_derecho, verde_frontal, amarillo_inferior)
    mostrar_cubo()

def inferior():
    print("Movimiento inferior")
    rotar_horario(amarillo_inferior, verde_frontal, rojo_lateral_derecho,
              azul_lateral_izquierdo, naranja_posterior)
    mostrar_cubo()

def inferior_primo():
    print("Movimiento inferior'")
    rotar_antihorario(amarillo_inferior, verde_frontal,
                  rojo_lateral_derecho, azul_lateral_izquierdo, naranja_posterior)
    mostrar_cubo()

def lateral_izquierdo():
    print("Movimiento lateral izquierdo")
    rotar_horario(azul_lateral_izquierdo, blanco_superior,
              naranja_posterior, amarillo_inferior, rojo_lateral_derecho)
    mostrar_cubo()

def lateral_izquierdo_primo():
    print("Movimiento lateral izquierdo'")
    rotar_antihorario(azul_lateral_izquierdo, blanco_superior,
                  naranja_posterior, amarillo_inferior, rojo_lateral_derecho)
    mostrar_cubo()

def posterior():
    print("Movimiento posterior")
    rotar_horario(naranja_posterior, blanco_superior, verde_frontal,
              amarillo_inferior, azul_lateral_izquierdo)
    mostrar_cubo()

def posterior_primo():
    print("Movimiento posterior'")
    rotar_horario(naranja_posterior, blanco_superior, verde_frontal,
              amarillo_inferior, azul_lateral_izquierdo)
    mostrar_cubo()



# Lista de funciones de movimiento disponibles
movimientos = [
    frontal, frontal_primo,
    lateral_derecho, lateral_derecho_primo,
    superior, superior_primo,
    inferior, inferior_primo,
    lateral_izquierdo, lateral_izquierdo_primo,
    posterior, posterior_primo
]

def desordenar_aleatoriamente():
    print("Desordenar de manera aleatoria")
    num_movimientos = random.randint(10, 20)  # Número aleatorio de movimientos
    for _ in range(num_movimientos):
        movimiento = random.choice(movimientos)  # Seleccionar un movimiento aleatorio
        movimiento()  # Ejecutar el movimiento
    mostrar_cubo()

def desordenar_dada_cantidad_movimientos():
    print("Desordenar dada una cantidad de movimientos")
    num_movimientos = int(input("Ingresa la cantidad de movimientos: "))
    for _ in range(num_movimientos):
        movimiento = random.choice(movimientos)  # Seleccionar un movimiento aleatorio
        movimiento()  # Ejecutar el movimiento
    mostrar_cubo()


def movimientos_manuales():
    while True:
        opcion = input(
            "Ingresa una opción \n 1: Frontal\n 2: Frontal' \n 3: Lateral derecho \n 4: Lateral derecho'\n 5: Superior\n 6:Superior' \n 7:Inferior \n 8:Inferior' \n 9: Lateral izquierdo \n 10: Lateral izquierdo' \n 11: Posterior \n 12: Posterior' \n 13: Salir\n"
        )
        if opcion == '13':
            break
        switcher = {
            '1': frontal,
            '2': frontal_primo,
            '3': lateral_derecho,
            '4': lateral_derecho_primo,
            '5': superior,
            '6': superior_primo,
            '7': inferior,
            '8': inferior_primo,
            '9': lateral_izquierdo,
            '10': lateral_izquierdo_primo,
            '11': posterior,
            '12': posterior_primo,
        }
        funcion = switcher.get(opcion)
        if funcion:
            funcion()
        else:
            print("Opción desconocida")

#=====================================================================================================================


def ordenar_cubo():
    matriz_cubo = [blanco_superior, amarillo_inferior, rojo_lateral_derecho, naranja_posterior, azul_lateral_izquierdo, verde_frontal]
    cubo_ordenado = [blanco_superior.copy(), amarillo_inferior.copy(), rojo_lateral_derecho.copy(), naranja_posterior.copy(), azul_lateral_izquierdo.copy(), verde_frontal.copy()]

    # Convertir las matrices del cubo en una lista para facilitar la ordenación
    lista_cubo = [elemento for matriz in matriz_cubo for fila in matriz for elemento in fila]

    # Ordenar la lista utilizando el algoritmo de búsqueda por burbuja
    n = len(lista_cubo)
    for i in range(n-1):
        for j in range(n-i-1):
            if lista_cubo[j] > lista_cubo[j+1]:
                lista_cubo[j], lista_cubo[j+1] = lista_cubo[j+1], lista_cubo[j]

    # Actualizar las matrices del cubo con la lista ordenada
    index = 0
    for matriz in cubo_ordenado:
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                matriz[i][j] = lista_cubo[index]
                index += 1

    # Actualizar las matrices originales del cubo con las matrices ordenadas
    blanco_superior[:] = cubo_ordenado[0]
    amarillo_inferior[:] = cubo_ordenado[1]
    rojo_lateral_derecho[:] = cubo_ordenado[2]
    naranja_posterior[:] = cubo_ordenado[5]
    azul_lateral_izquierdo[:] = cubo_ordenado[4]
    verde_frontal[:] = cubo_ordenado[3]


    mostrar_cubo()


#=====================================================================================================================
# Matrices iniciales
blanco_superior = [["W", "W", "W"], ["W", "W", "W"], ["W", "W", "W"]]
amarillo_inferior = [["Y", "Y", "Y"], ["Y", "Y", "Y"], ["Y", "Y", "Y"]]
rojo_lateral_derecho = [["R", "R", "R"], ["R", "R", "R"], ["R", "R", "R"]]
naranja_posterior = [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]
azul_lateral_izquierdo = [["B", "B", "B"], ["B", "B", "B"], ["B", "B", "B"]]
verde_frontal = [["G", "G", "G"], ["G", "G", "G"], ["G", "G", "G"]]



mostrar_cubo()
while True:
    opcion = input(
        "Ingresa una opción \n 1: Movimientos manuales\n 2: Desordenar de manera aleatoria \n 3: Desordenar dada una cantidad de movimientos \n 4: Mostrar cubo\n 5: Ordenar cubo \n 6: Salir\n"
    )
    if opcion == '6':
        break
    switcher = {
        '1': movimientos_manuales,
        '2': desordenar_aleatoriamente,
        '3': desordenar_dada_cantidad_movimientos,
        '4': mostrar_cubo,
        '5': ordenar_cubo,
    }
    funcion = switcher.get(opcion)
    if funcion:
        funcion()
    else:
        print("Opción desconocida")
