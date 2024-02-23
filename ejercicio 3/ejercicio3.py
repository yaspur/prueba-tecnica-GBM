def calculo_min_steps(x):
        
        # Iniciamos variables para llevar control de la posicion, cuantos saltos dar, e ir aumentando la cantidad de veces

        i = 1 # para llevarla sumatoria de cuantos saltos realizar en la siguiente iteracion
        posicion_actual = 0 
        saltos = 0

        while posicion_actual < x:

            # en cada iteracion se toma el valor de i y se le suma a la posicion actual, asi iria +1 +2 +3
            posicion_actual += i
            i += 1
            saltos += 1 # Aumentar la cantidad de saltos
        
        if(posicion_actual == x):
            # Si la posicion actual llego al numero de saltos entonces devolver los saltos
            return saltos
        else:
            calcular_diferencia = posicion_actual - x
            if(calcular_diferencia == 1):
                return saltos + 1
            else:
                return saltos


def steps():
    
    casos_prueba = int(input("Ingrese el numero de casos de prueba: "))

    for casos_prueba in range(casos_prueba):

        x = int(input("Ingrese  el valor donde quiere dirigirse: "))
        print("El numero de saltos es: ", calculo_min_steps(x))

if __name__ == '__main__':
     steps()

        



