import random

# Crear una matriz 3x3 con valores iniciales
def crear_cara(color, nombre):
    return {"nombre": nombre, "matriz": [[color] * 3 for _ in range(3)]}

# Crear el cubo de Rubik con todas las caras
def crear_cubo():
    cubo = {
      "frontal": crear_cara("⬜️", "Frontal"),
        "trasera": crear_cara("🟨", "Trasera"),
        "superior": crear_cara("🟧", "Superior"),
        "inferior": crear_cara("🟥", "Inferior"),
        "derecha": crear_cara("🟩", "Derecha"),
        "izquierda": crear_cara("🟦", "Izquierda")   
    }
    return cubo

# Realizar el movimiento R (giro a la derecha de la cara frontal)
def movimiento_r(cubo):
    # Girar la cara frontal
    cubo["frontal"]["matriz"] = list(map(list, zip(*reversed(cubo["frontal"]["matriz"]))))
    
    # Guardar los elementos afectados por el movimiento
    temp1 = cubo["superior"]["matriz"][0][2]
    temp2 = cubo["superior"]["matriz"][1][2]
    temp3 = cubo["superior"]["matriz"][2][2]
    temp4 = cubo["inferior"]["matriz"][0][2]
    temp5 = cubo["inferior"]["matriz"][1][2]
    temp6 = cubo["inferior"]["matriz"][2][2]
    
    # Mover los elementos de las caras afectadas
    cubo["superior"]["matriz"][0][2] = cubo["izquierda"]["matriz"][0][2]
    cubo["superior"]["matriz"][1][2] = cubo["izquierda"]["matriz"][1][2]
    cubo["superior"]["matriz"][2][2] = cubo["izquierda"]["matriz"][2][2]
    
    cubo["inferior"]["matriz"][0][2] = cubo["derecha"]["matriz"][0][2]
    cubo["inferior"]["matriz"][1][2] = cubo["derecha"]["matriz"][1][2]
    cubo["inferior"]["matriz"][2][2] = cubo["derecha"]["matriz"][2][2]
    
    cubo["derecha"]["matriz"][0][2] = temp1
    cubo["derecha"]["matriz"][1][2] = temp2
    cubo["derecha"]["matriz"][2][2] = temp3
    
    # Mover la columna del medio sin afectar el elemento del medio
    cubo["izquierda"]["matriz"][0][2] = cubo["trasera"]["matriz"][0][2]
    cubo["izquierda"]["matriz"][1][2] = cubo["trasera"]["matriz"][1][2]
    cubo["izquierda"]["matriz"][2][2] = cubo["trasera"]["matriz"][2][2]
    
    cubo["trasera"]["matriz"][0][2] = temp4
    cubo["trasera"]["matriz"][1][2] = temp5
    cubo["trasera"]["matriz"][2][2] = temp6
    
    return cubo

# Realizar el movimiento F (giro hacia adelante de la cara superior)
def movimiento_f(cubo):
    # Girar la cara superior
    cubo["superior"]["matriz"] = list(map(list, zip(*reversed(cubo["superior"]["matriz"]))))
    
    # Guardar los elementos afectados por el movimiento
    temp1 = cubo["frontal"]["matriz"][0][0]
    temp2 = cubo["frontal"]["matriz"][1][0]
    temp3 = cubo["frontal"]["matriz"][2][0]
    
    # Mover los elementos de las caras afectadas
    cubo["frontal"]["matriz"][0][0] = cubo["izquierda"]["matriz"][0][0]
    cubo["frontal"]["matriz"][1][0] = cubo["izquierda"]["matriz"][1][0]
    cubo["frontal"]["matriz"][2][0] = cubo["izquierda"]["matriz"][2][0]
    
    cubo["izquierda"]["matriz"][0][0] = cubo["trasera"]["matriz"][0][0]
    cubo["izquierda"]["matriz"][1][0] = cubo["trasera"]["matriz"][1][0]
    cubo["izquierda"]["matriz"][2][0] = cubo["trasera"]["matriz"][2][0]
    
    cubo["trasera"]["matriz"][0][0] = cubo["derecha"]["matriz"][0][0]
    cubo["trasera"]["matriz"][1][0] = cubo["derecha"]["matriz"][1][0]
    cubo["trasera"]["matriz"][2][0] = cubo["derecha"]["matriz"][2][0]
    
    cubo["derecha"]["matriz"][0][0] = temp1
    cubo["derecha"]["matriz"][1][0] = temp2
    cubo["derecha"]["matriz"][2][0] = temp3
    
    return cubo

# Realizar el movimiento Rah (giro a la derecha de la cara frontal en sentido antihorario)
def movimiento_rah(cubo):
    # Girar la cara frontal en sentido antihorario
    cubo["frontal"]["matriz"] = list(map(list, zip(*cubo["frontal"]["matriz"])))[::-1]
    
    # Guardar los elementos afectados por el movimiento
    temp1 = cubo["superior"]["matriz"][0][2]
    temp2 = cubo["superior"]["matriz"][1][2]
    temp3 = cubo["superior"]["matriz"][2][2]
    temp4 = cubo["inferior"]["matriz"][0][2]
    temp5 = cubo["inferior"]["matriz"][1][2]
    temp6 = cubo["inferior"]["matriz"][2][2]
    
    # Mover los elementos de las caras afectadas
    cubo["superior"]["matriz"][0][2] = cubo["izquierda"]["matriz"][0][2]
    cubo["superior"]["matriz"][1][2] = cubo["izquierda"]["matriz"][1][2]
    cubo["superior"]["matriz"][2][2] = cubo["izquierda"]["matriz"][2][2]
    
    cubo["inferior"]["matriz"][0][2] = cubo["derecha"]["matriz"][0][2]
    cubo["inferior"]["matriz"][1][2] = cubo["derecha"]["matriz"][1][2]
    cubo["inferior"]["matriz"][2][2] = cubo["derecha"]["matriz"][2][2]
    
    cubo["derecha"]["matriz"][0][2] = temp1
    cubo["derecha"]["matriz"][1][2] = temp2
    cubo["derecha"]["matriz"][2][2] = temp3
    
    # Mover la columna del medio sin afectar el elemento del medio
    cubo["izquierda"]["matriz"][0][2] = cubo["trasera"]["matriz"][0][2]
    cubo["izquierda"]["matriz"][1][2] = cubo["trasera"]["matriz"][1][2]
    cubo["izquierda"]["matriz"][2][2] = cubo["trasera"]["matriz"][2][2]
    
    cubo["trasera"]["matriz"][0][2] = temp4
    cubo["trasera"]["matriz"][1][2] = temp5
    cubo["trasera"]["matriz"][2][2] = temp6
    
    return cubo

# Mostrar el cubo en pantalla
def mostrar_cubo(cubo):
    # Imprimir la cara superior
    cara_superior = cubo["superior"]
    print("      ", end="")
    for _ in range(3):
        print("      ", end="")
    for elemento in cara_superior["matriz"][0]:
        print(elemento, end=" ")
    print() 

    print("      ", end="")
    for _ in range(3):
        print("      ", end="")
    for elemento in cara_superior["matriz"][1]:
        print(elemento, end=" ")
    print()

    print("      ", end="")
    for _ in range(3):
        print("      ", end="")
    for elemento in cara_superior["matriz"][2]:
        print(elemento, end=" ")
    print()

    print()

 # Imprimir la cara izquierda y la frontal
    cara_derecha = cubo["derecha"]
    cara_frontal = cubo["frontal"]
    cara_izquierda = cubo["izquierda"]
    cara_trasera = cubo["trasera"]
    for fila_derecha, fila_frontal, fila_izquierda, fila_trasera in zip(cara_derecha["matriz"], cara_frontal["matriz"], cara_izquierda["matriz"], cara_trasera["matriz"]):
        print("       ", end="")
        for elemento in fila_derecha:
            print(elemento, end=" ")
        print("        ", end="")
        for elemento in fila_frontal:
            print(elemento, end=" ")
        print("       ", end="")
        for elemento in fila_izquierda:
            print(elemento, end=" ")
        print("      ", end="")
        for elemento in fila_trasera:
            print(elemento, end=" ")
        print()


    # Imprimir la cara inferior
    print()
    cara_inferior = cubo["inferior"]
    print("      ", end="")
    for _ in range(3):
        print("      ", end="")
    for elemento in cara_inferior["matriz"][0]:
        print(elemento, end=" ")
    print()

    print("      ", end="")
    for _ in range(3):
        print("      ", end="")
    for elemento in cara_inferior["matriz"][1]:
        print(elemento, end=" ")
    print()

    print("      ", end="")
    for _ in range(3):
        print("      ", end="")
    for elemento in cara_inferior["matriz"][2]:
        print(elemento, end=" ")
    print()

    print()

      
#  Función desordenar_cubo() para aceptar el número de movimientos
def desordenar_cubo(cubo, movimientos):
    contador_movimientos = 0  # Variable para contar los movimientos realizados
    for _ in range(movimientos):
        movimiento_aleatorio = random.choice([movimiento_r, movimiento_f, movimiento_rah])
        cubo = movimiento_aleatorio(cubo)
        contador_movimientos += 1
    print(f"Se realizaron {contador_movimientos} movimientos al desordenar el cubo.")
    return cubo

#  Función menu() para que el usuario ingrese lo que desea
def menu():
    cubo = crear_cubo()
    opcion = 0

    while opcion != '4':
        print("\n---------- MENÚ ----------")
        print("1. Mostrar el cubo de Rubik")
        print("2. Desordenar el cubo")
        print("3. Ordenar el cubo")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            mostrar_cubo(cubo)
        elif opcion == '2':
            movimientos = int(input("Ingrese el número de movimientos para desordenar el cubo: "))
            cubo = desordenar_cubo(cubo, movimientos)
            print("\nCubo desordenado:")
            mostrar_cubo(cubo)
        elif opcion == '3':
            cubo = crear_cubo()
            print("\nCubo ordenado:")
            mostrar_cubo(cubo)
        elif opcion == '4':
            print("Usted ha salido del programa, tenga un buen dia!")
        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecutar el menú
menu()