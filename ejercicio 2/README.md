# Ejercicio 2: Formula 1

Este ejercicio nos pide que por medio de los resultados de las carreras en una temporada  se calcule quien es el campeon mundial para diferentes sistemas de puntuacion.

## Como ejecutar el codigo:
1.  Tener python instalado n la computadora
2. Tener la carpeta `ejercicio 2` descargada y verificar que contenga los archivos:
	- **ejercicio2.py:** contiene algoritmo para  dar solucion al problema
	
	####TESTS
	- test_ejercicio2.py
	- test2_ejercicio2.py
	- test3_ejercicio2.py

3.  Abrir la terminal y dirigirse a la ubicacion donde estan los archivos .py
4. Dentro de la ruta ejecutar el comando `python ejercicio2.py`
	- En la terminal el programa te pedira los datos que necesita para poder hacer el calculo

## Input / Entradas

1.  Escribir el numero de carreras que se realizaron y el numero de pilotos **separados por un espacio** es decir: `1 3`, aqui contempla 1 carrera y 3 pilotos.

2. Por cada carrera nos va a pedir el orden de llegada de los pilotos **separados por un  espacio**, es decir si se le pasa `10 4 6` el piloto*10* llego en primera posicion, el piloto *4* llego en segunda posicion, el piloto *6* llego en tercera posicion.

3. Escribir el numero de sistemas de puntuacion, es decir, cuantos sistemas de puntuacion vamos a evaluar, y por cada sistema de puntuacion obtendremos quien o quienes fueron los campeones para cada sistema, ejemplo `3`, se van a evaluar 3 sistemas de puntuaciony determinar el campeon para cada uno.

4. Por cada sistema de puntuacion el programa nos pedira 2 datos:
	- Primero nos pedira el numero de pilotos que recibiran puntos, por ejemplo, si escribimos `3` solos los 3 primeros pilotos recibiran puntos.

	- como segundo dato nos pedira los puntos para cada posicion de llegada **separado por espacios**, es decir, si ingresamos `10 8 6`, al  primer puesto se le daran *10* puntos, al segundo puesto se le daran *8* puntos, y al tercer puesto se le daran *6* puntos.

## Output / salida
El programa nos dara una respuesta por cada sistema de puntuacion, mostrandonos quien fue el campeon para cada sistema en la terminal.

####  Ejemplo
Si se le paso 1 solo sistema solo recibiremos una respuesta
`Campeon(es) del mundo son: 1`

si la cantidad de sistemas es de 2 en adelante el programa nos mostrara cada resultado en una linea en la terminal.

## Ejecutar pruebas unitarias
Para  ejecutar las pruebas se debe estar dentro de la ruta donde estan los archivos, es decir donde se hizo la ejecucion del codigo

correr el siguiente comando `python test_ejercicio2` y en la terminal veremos el resultado 

para correr las demas pruebas solo es colocar en la terminal `python nombre_test.py` en **nombre_test.py** se debe colocar el nombre del archivo a probar.


Con esta Url se puede probar el codigo online

https://colab.research.google.com/drive/1C6FOJsJnf75_X-r0bNPY9y35ThONr7q8?usp=sharing