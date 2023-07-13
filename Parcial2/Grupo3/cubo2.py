class CuboRubik:
    def __init__(self):
        self.caras = {
            'frontal': [['🟥'] * 3 for _ in range(3)],
            'trasera': [['🟧'] * 3 for _ in range(3)],
            'izquierda': [['🟨'] * 3 for _ in range(3)],
            'derecha': [['🟩'] * 3 for _ in range(3)],
            'superior': [['🟦'] * 3 for _ in range(3)],
            'inferior': [['🟪'] * 3 for _ in range(3)]
        }

    def girar_cara_sentido_horario(self, cara):
        self.caras[cara] = [list(fila[::-1]) for fila in zip(*self.caras[cara])]

    def girar_cara_sentido_antihorario(self, cara):
        self.caras[cara] = [list(fila) for fila in zip(*self.caras[cara][::-1])]

    def girar_cara_180(self, cara):
        self.girar_cara_sentido_horario(cara)
        self.girar_cara_sentido_horario(cara)

    def girar_sentido_horario(self, cara):
        self.girar_cara_sentido_horario(cara)
        if cara == 'frontal':
            self.caras['superior'][2][:], self.caras['derecha'][0][:], self.caras['inferior'][0][:], self.caras['izquierda'][2][:] = \
                self.caras['izquierda'][2][:], self.caras['superior'][2][:], self.caras['derecha'][0][:], self.caras['inferior'][0][:]
        elif cara == 'trasera':
            self.caras['superior'][0][:], self.caras['izquierda'][0][:], self.caras['inferior'][2][:], self.caras['derecha'][2][:] = \
                self.caras['derecha'][2][:], self.caras['superior'][0][:], self.caras['izquierda'][0][:], self.caras['inferior'][2][:]
        elif cara == 'izquierda':
            self.caras['superior'][0][:], self.caras['trasera'][0][:], self.caras['inferior'][0][:], self.caras['frontal'][0][:] = \
                self.caras['frontal'][0][:], self.caras['superior'][0][:], self.caras['trasera'][0][:], self.caras['inferior'][0][:]
        elif cara == 'derecha':
            self.caras['superior'][2][:], self.caras['frontal'][2][:], self.caras['inferior'][2][:], self.caras['trasera'][2][:] = \
                self.caras['trasera'][2][:], self.caras['superior'][2][:], self.caras['frontal'][2][:], self.caras['inferior'][2][:]
        elif cara == 'superior':
            self.caras['frontal'][0][:], self.caras['derecha'][0][:], self.caras['trasera'][0][:], self.caras['izquierda'][0][:] = \
                self.caras['izquierda'][0][:], self.caras['frontal'][0][:], self.caras['derecha'][0][:], self.caras['trasera'][0][:]
            self.caras['frontal'][1][:], self.caras['derecha'][1][:], self.caras['trasera'][1][:], self.caras['izquierda'][1][:] = \
                self.caras['izquierda'][1][:], self.caras['frontal'][1][:], self.caras['derecha'][1][:], self.caras['trasera'][1][:]
            self.caras['frontal'][2][:], self.caras['derecha'][2][:], self.caras['trasera'][2][:], self.caras['izquierda'][2][:] = \
                self.caras['izquierda'][2][:], self.caras['frontal'][2][:], self.caras['derecha'][2][:], self.caras['trasera'][2][:]
        elif cara == 'inferior':
            self.caras['frontal'][2][:], self.caras['izquierda'][2][:], self.caras['trasera'][2][:], self.caras['derecha'][2][:] = \
                self.caras['derecha'][2][:], self.caras['frontal'][2][:], self.caras['izquierda'][2][:], self.caras['trasera'][2][:]
            self.caras['frontal'][1][:], self.caras['izquierda'][1][:], self.caras['trasera'][1][:], self.caras['derecha'][1][:] = \
                self.caras['derecha'][1][:], self.caras['frontal'][1][:], self.caras['izquierda'][1][:], self.caras['trasera'][1][:]
            self.caras['frontal'][0][:], self.caras['izquierda'][0][:], self.caras['trasera'][0][:], self.caras['derecha'][0][:] = \
                self.caras['derecha'][0][:], self.caras['frontal'][0][:], self.caras['izquierda'][0][:], self.caras['trasera'][0][:]

    def armar(self):
        self.caras = {
            'frontal': [['🟥'] * 3 for _ in range(3)],
            'trasera': [['🟧'] * 3 for _ in range(3)],
            'izquierda': [['🟨'] * 3 for _ in range(3)],
            'derecha': [['🟩'] * 3 for _ in range(3)],
            'superior': [['🟦'] * 3 for _ in range(3)],
            'inferior': [['🟪'] * 3 for _ in range(3)]
        }

    def mezclar(self, movimientos=20):
        import random
        for _ in range(movimientos):
            cara = random.choice(list(self.caras.keys()))
            sentido_horario = random.choice([True, False])
            if sentido_horario:
                self.girar_sentido_horario(cara)
            else:
                self.girar_cara_sentido_antihorario(cara)

    def mostrar(self):
        print("------ Estado actual del cubo ------")
        print("Cara Frontal:")
        for fila in self.caras['frontal']:
            print('\t\t', end='')
            print(' '.join(fila))
        print("\nCara Trasera:")
        for fila in self.caras['trasera']:
            print('\t\t', end='')
            print(' '.join(fila))
        print("\nCara Izquierda:")
        for fila in self.caras['izquierda']:
            print('\t\t', end='')
            print(' '.join(fila))
        print("\nCara Derecha:")
        for fila in self.caras['derecha']:
            print('\t\t', end='')
            print(' '.join(fila))
        print("\nCara Superior:")
        for fila in self.caras['superior']:
            print('\t\t', end='')
            print(' '.join(fila))
        print("\nCara Inferior:")
        for fila in self.caras['inferior']:
            print('\t\t', end='')
            print(' '.join(fila))
        print()


def mostrar_menu():
    print("------ Menú ------")
    print("1. Armar el cubo")
    print("2. Mezclar el cubo")
    print("3. Girar una cara en sentido horario")
    print("4. Girar una cara en sentido antihorario")
    print("5. Mostrar el estado actual del cubo")
    print("0. Salir")


cubo = CuboRubik()

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        cubo.armar()
        print("El cubo ha sido armado.")
    elif opcion == '2':
        movimientos = int(input("Ingrese el número de movimientos para mezclar el cubo: "))
        cubo.mezclar(movimientos)
        print("El cubo ha sido mezclado.")
    elif opcion == '3':
        cara = input("Ingrese la cara a girar en sentido horario (frontal, trasera, izquierda, derecha, superior, inferior): ")
        cubo.girar_sentido_horario(cara)
        print(f"La cara {cara} ha sido girada en sentido horario.")
    elif opcion == '4':
        cara = input("Ingrese la cara a girar en sentido antihorario (frontal, trasera, izquierda, derecha, superior, inferior): ")
        cubo.girar_cara_sentido_antihorario(cara)
        print(f"La cara {cara} ha sido girada en sentido antihorario.")
    elif opcion == '5':
        cubo.mostrar()
    elif opcion == '0':
        break
    else:
        print("Opción inválida. Intente nuevamente.")

    print()
