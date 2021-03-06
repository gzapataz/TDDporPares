class Estadisticas:
    def calcular(self, cadena):
        cadenaResp = [0, 0, 0, 0]

        if cadena == "":
            cadenaResp[0] = 0 #numero de elementos
            cadenaResp[1] = 0 #minimo en la secuencia
            cadenaResp[2] = 0 #maximo en la secuencia
            cadenaResp[3] = 0  # promedio en la secuencia

        elif "," not in cadena:
            cadenaResp[0] = 1
            cadenaResp[1] = int(cadena)
            cadenaResp[2] = int(cadena)
            cadenaResp[3] = int(cadena)
        else:
            numeros = cadena.split(",")
            i = 0
            minimo = int(numeros[0]) #La primera vez se asume que el minimo viene en la primera posicion, luego viene la comparacion
            maximo = int(numeros[0]) # La primera vez se asume que el maximo viene en la primera posicion, luego viene la comparacion
            suma = 0.0

            for num in numeros:
                i = i+1
                if int(num) < int(minimo):
                    minimo=int(num)

                if int(num) > int(maximo):
                    maximo=int(num)

                suma = suma + int(num)

            cadenaResp[0] = i
            cadenaResp[1] = int(minimo)
            cadenaResp[2] = int(maximo)
            cadenaResp[3] = suma / i

        return cadenaResp