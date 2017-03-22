class Estadisticas:
    def calcular(self, cadena):
        cadenaResp = [0, 0]

        if cadena == "":
            cadenaResp[0] = 0
            cadenaResp[1] = 0
        elif "," not in cadena:
            cadenaResp[0] = 1
            cadenaResp[1] = int(cadena)
        else:
            numeros = cadena.split(",")
            i = 0
            for num in numeros:
                i = i+1
            cadenaResp[0] = i

        return cadenaResp