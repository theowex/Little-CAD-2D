def actualizar_pantalla(matriz):
    for j in range(43, -1, -1):
        for i in range(84):
            print(matriz[j][i], end = " ")
        print()
    return matriz

def agregar_segmento(x1, y1, x2, y2, matriz):
    x = x2 - x1
    y = y2 - y1
    if x1 == x2:
        for i in range(abs(y)):
            matriz[min(y1, y2) + i][x1] = "X"
        matriz[max(y1, y2)][x1] = "X"
    else:
        m = float(y / x)
        rango = max(abs(x), abs(y))
        iterador = float((x / abs(x)) * (abs(x) / rango))
        ix = 0
        for i in range(rango):
            iy = float(m * ix)
            matriz[round(y1 + iy)][round(x1 + ix)] = "X"
            ix += iterador
        matriz[y2][x2] = "X"
    return matriz

def agregar_linea(matriz):
    print("Ingrese la coordenada de origen")
    x1 = int(input("Ingrese x: "))
    y1 = int(input("Ingrese y: "))
    print("Ingrese la coordenada final")
    x2 = int(input("Ingrese x: "))
    y2 = int(input("Ingrese y: "))
    agregar_segmento(x1, y1, x2, y2, matriz)
    return matriz

def agregar_rectangulo_cuadrado(matriz):
    print("Ingrese la coordenada de origen")
    x1 = int(input("Ingrese x: "))
    y1 = int(input("Ingrese y: "))
    b = int(input("Ingrese la base: "))
    h = int(input("Ingrese la altura: "))
    agregar_segmento(x1, y1, x1 + b - 1, y1, matriz)
    agregar_segmento(x1 + b - 1, y1, x1 + b - 1, y1 + h - 1, matriz)
    agregar_segmento(x1 + b - 1, y1 + h - 1, x1, y1 + h - 1, matriz)
    agregar_segmento(x1, y1 + h - 1, x1, y1, matriz)
    return matriz

def agregar_triangulo(matriz):
    print("Ingrese la coordenada de origen")
    x1 = int(input("Ingrese x: "))
    y1 = int(input("Ingrese y: "))
    b = int(input("Ingrese la base: "))
    h = int(input("Ingrese la altura: "))
    agregar_segmento(x1, y1, x1 + b - 1, y1, matriz)
    agregar_segmento(x1 + b - 1, y1, x1 + b//2, y1 + h - 1, matriz)
    agregar_segmento(x1 + b - 1 - b//2, y1 + h - 1, x1, y1, matriz)
    return matriz

def agregar_elipse_circulo(matriz):
    x1 = int(input("Ingrese x: "))
    y1 = int(input("Ingrese y: "))
    a = int(input("Radio base: "))
    b = int(input("Radio altura: "))
    rango = 1000
    iterador = float(abs(2 * a) / rango)
    ix = 0 - a
    for i in range(rango):
        iy = (b / a) * (((a ** 2) - (ix ** 2))**(1/2))
        matriz[round(y1 + iy)][round(x1 + ix)] = "X"
        matriz[round(y1 - iy)][round(x1 + ix)] = "X"
        ix += iterador
    matriz[y1][x1 + a] = "X"
    return matriz


