import opciones
import almacenar

matriz = []
matrizx = []
for i in range(84):
    matrizx.append(" ")
for j in range(44):
    matriz.append(matrizx[::])
for j in range(44):
    matriz[j][0] = "."
    matriz[j][83] = "."
for i in range(84):
    matriz[0][i] = "."
    matriz[43][i] = "."

def menu(matriz):
    print("Menú")
    print("1.  Agregar una línea")
    print("2.  Agregar una elipse o circulo")
    print("3.  Agregar un rectángulo o cuadrado")
    print("4.  Agregar un triangulo")
    print("5.  Mostrar un dibujo")
    print("6.  Leer un dibujo")
    print("7.  Grabar un dibujo")
    print("\n0.  Salir del programa\n")
    opcion = int(input("Ingrese la opción que desee: "))
    while opcion < 0 or opcion > 7:
        opcion = int(input("Esa opción no existe. Por favor ingrese un valor válido: "))
    if opcion == 0:
        return False
    elif opcion == 1:
        opciones.agregar_linea(matriz)
    elif opcion == 2:
        opciones.agregar_elipse_circulo(matriz)
    elif opcion == 3:
        opciones.agregar_rectangulo_cuadrado(matriz)
    elif opcion == 4:
        opciones.agregar_triangulo(matriz)
    elif opcion == 5:
        print("")
        #matriz = opciones.mostrar_dibujo(matriz)
    elif opcion == 6:
        almacenar.leer_dibujo(matriz)
    elif opcion == 7:
        almacenar.grabar_dibujo(matriz)
    opciones.actualizar_pantalla(matriz)
    return True

def iniciar(est):
    opciones.actualizar_pantalla(matriz)
    while est == True:
        est = menu(matriz)

iniciar(True)