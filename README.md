# Little CAD 2D

## Descripción del Programa:
El programa generará dibujos de círculos o elipses, triángulos, rectangulos o cuadrados y líneas. Así mismo puede leer y grabar un dibujo. Para esto se usó matrices, mediante las cuales se logró establcer un eje coordenado
```python
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
```
Para lograr dibujar, se crearon funciones en donde se usaba la ecuación de la recta y la elipse.


## Instrucciones de uso:
<br>Al inicio del programa se presentará un menú, aquí se mostrarán las siguientes opciones, en donde cada una represanta un número:</br>
<br>Agregar una línea: Número 1</br>
<br>Agregar una elipse o circulo: Número 2</br>
<br>Agregar un rectángulo o cuadrado: Número 3</br>
<br>Agregar un triangulo: Número 4</br>
<br>Mostrar un dibujo: Número 5</br>
<br>Leer un dibujo: Número 6</br>
<br>Grabar un dibujo: Número 7</br>
<br>Salir del programa: Número 0</br>
<br>Posteriorme se ingresará el número que representa el gráfico a dibujar, dependiendo del gráfico usado se mostrarán distintas opciones. </br>
<br>En el caso de leer dibujo y grabar dibujo, se debe ingreser el nombre del archivo a importar y exportar respectivamente.</br>
<br>Para ingresar librerias:</br>

```python
import opciones
import almacenar
```


## Restricciones:
<br>-Solo se pueden importar archivos con extensión ".txt" y se distingue mayusculas y minúsculas.</br>
<br>-En todos los dibujos se deben ingresar valores entre los rangos, comenzando desde 1. En el caso del alto va desde 1 hasta 42, en el caso del ancho va desde 1 hasta 82</br>
<br>-Si los valores ingresados no se encuentran en el rango</br>
<br>-Los archivos deben encontrarse en la misma carpeta donde se encuentra el archivo del programa</br>
<br>-Para ingresar dibujar una circunferencia, radio base debe ser igual a radio altura</br>



## Integrantes:
<br>-Atamari Aldazabal, Owen</br>
<br>-Abanto Rodriguez, Diego</br>
<br>-Bustamante Yep, Joaquín</br>

## Universidad
[![alt text](https://www.utec.edu.pe/sites/default/files//logo_0.png)](https://www.utec.edu.pe/)
