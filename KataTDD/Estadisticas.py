class Estadisticas:
    def calcular(self, cadena):
        cadenaResp = [0]
        cadenaResp[0] = 0

        if cadena == "":
            return cadenaResp
        elif "," not in cadena:
            cadenaResp[0] = 1
            return cadenaResp
