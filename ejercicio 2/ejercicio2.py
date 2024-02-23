def definir_campeon(posiciones, sistema):

    # Definimos K como cuantos pilotos recibiran puntos
    # y una lista con los puntos
    K, puntos = sistema
    
    puntuacion = {}

    puntaje_maximo = 0

    for carrera in posiciones:
        for j in range(K):

            if str(carrera[j]) not in puntuacion:
                puntuacion[str(carrera[j])] = puntos[j]
            else:
                puntuacion[str(carrera[j])] += puntos[j]
            
    puntaje_maximo = max(puntuacion.values())

    campeones = set()

    # Iterar a través del diccionario para encontrar las claves que tienen el valor máximo y agregarlas al conjunto
    for clave, valor in puntuacion.items():
        if valor == puntaje_maximo:
            campeones.add(clave)

    return campeones
            



def main():

    while True:

        # Obtener los datos de carreras y pilotos 
        grand_pix_pilots = input("Ingrese el numero de Carreras y el numero de Pilotos separados por espacio: ").split()
        #  Convertir los datos en una lista de numeros para poder manipularlos
        G, P = [int(x) for x in grand_pix_pilots]
        
        # Detener el programa si el user ingresa 0 0
        if G == 0 and P == 0:
            break
        
        # Ingresar posiciones de los pilotos
        posiciones = []
        for race in range(G):
            posiciones_race = input("Ingrese el orden de llegada de los pilotos en la carrera separados por espacio: ").split()
            posiciones_race = [int(lugar) for lugar in posiciones_race]
            posiciones.append(posiciones_race)

        # Ingresar cantidad de sistemas de puntuacion
        S = int(input("Ingrese el numero de sistemas de puntuacion: "))

        # Por cada sistema de puntuacion pedir al usuario los valores a tener en cuenta
        sistemas_puntuacion = []
        for sistema in range(S):
            #  Solicitar cuantos pilotos recibiran puntos
            K = int(input("Ingrese cuantos pilotos recibiran puntos: "))
            # Solicitar los puntospara cada posicion
            puntos = input("Ingrese los puntos obtenidos para cada posicion en orden de llegada: ").split()
            puntos = [int(x) for x in puntos]
            sistemas_puntuacion.append((K, puntos))

        
        # Por cada sistema de puntuacion sumar puntos y devolver el campeon
        for sistema in sistemas_puntuacion:
            # definir campeon
            campeon = definir_campeon(posiciones, sistema)
            print('Campon(es) del mundo son: ', *campeon)
            return campeon
        

if __name__ == '__main__':
    main()