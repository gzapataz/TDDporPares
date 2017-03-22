class Estadisticas:
    def calcular(self, cadena):
        cadenaResp = [0, 0, 0]

        if cadena == "":
            cadenaResp[0] = 0 #numero de elementos
            cadenaResp[1] = 0 #minimo en la secuencia
            cadenaResp[2] = 0 #maximo en la secuencia

        elif "," not in cadena:
            cadenaResp[0] = 1
            cadenaResp[1] = int(cadena)
            cadenaResp[2] = int(cadena)
        else:
            numeros = cadena.split(",")
            i = 0
            minimo = int(numeros[0]) #La primera vez se asume que el minimo viene en la primera posicion, luego viene la comparacion
            maximo = int(numeros[0]) # La primera vez se asume que el maximo viene en la primera posicion, luego viene la comparacion

            for num in numeros:
                i = i+1
                if int(num) < int(minimo):
                    minimo=int(num)

                if int(num) > int(maximo):
                    maximo=int(num)

            cadenaResp[0] = i
            cadenaResp[1] = int(minimo)
            cadenaResp[2] = int(maximo)

        return cadenaResp