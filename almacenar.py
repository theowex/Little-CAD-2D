def leer_dibujo(matriz):
    nombre = input("Ingrese el nombre del archivo: ")
    archivo = open(nombre + ".txt", "r")
    texto = archivo.readlines()
    print(texto)
    for j in range(44):
        lista = list(texto[j])
        #print(lista)
        for i in range(84):
            matriz[- (j + 1)][i] = lista[i*2]
    archivo.close()
    return matriz

def grabar_dibujo(matriz):
    nombre = input("Ingrese el nombre del archivo: ")
    try:
        open(nombre + ".txt", "x")
    except FileExistsError:
        print("")
    archivo = open(nombre + ".txt", "w")
    palabra = ""
    for j in range(43, -1, -1):
        for i in range(84):
            palabra = palabra + matriz[j][i] + " "
        palabra += "\n"
    archivo.write(palabra)
    archivo.close()
    return matriz