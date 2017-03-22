from unittest import TestCase
from Estadisticas import Estadisticas


class EstadisticasTest(TestCase):
    #Paso 1 Devolver un arreglo con el numero de elementos

    #Iteracion 1
    def test_calcular(self):
        self.assertEqual(Estadisticas().calcular("")[0], 0, "String Vacio")

    # Iteracion 2
    def test_calcular_un_numero(self):
        self.assertEqual(Estadisticas().calcular("25")[0], 1, "Ciclo un Numero")

    # Iteracion 3
    def test_calcular_dos_numeros(self):
        self.assertEqual(Estadisticas().calcular("25,10")[0], 2, "Ciclo con dos numeros, devuelve numero de elementos")

    # Iteracion 4
    def test_calcular_varios_numeros(self):
        self.assertEqual(Estadisticas().calcular("25,10,12")[0], 3, "Ciclo con varios numeros, devuelve numero de elementos")


    #Paso 2 Devolver un arreglo con el numero de elementos y el minimo

    # Iteracion 1
    def test_calcular(self):
        self.assertEqual(Estadisticas().calcular("")[1], 0, "String Vacio y minimo")

    # Iteracion 2
    def test_calcular_un_numero(self):
        self.assertEqual(Estadisticas().calcular("25")[0],1, "Ciclo un Numero")
        self.assertEqual(Estadisticas().calcular("25")[1], 25, "Minimo un Numero")

    # Iteracion 3
    def test_calcular_dos_numeros(self):
        self.assertEqual(Estadisticas().calcular("25,10")[1], 10, "Ciclo con dos numeros, devuelve el minimo de los dos")
        self.assertEqual(Estadisticas().calcular("11,40")[1], 11, "Ciclo con dos numeros, devuelve el minimo de los dos")

    # Iteracion 4
    def test_calcular_dos_numeros_minimo(self):
        self.assertEqual(Estadisticas().calcular("25,10, 9")[1], 9, "Ciclo con varios numeros, devuelve el minimo de los dos")


    #Paso 3 Devolver un arreglo con el numero de elementos y el minimo y el maximo

    #Iteracion 1
    def test_calcular_maximo(self):
        self.assertEqual(Estadisticas().calcular("")[1], 0, "String Vacio y minimo")
        self.assertEqual(Estadisticas().calcular("")[2], 0, "String Vacio y maximo")

    # Iteracion 2
    def test_calcular_un_numero(self):
        self.assertEqual(Estadisticas().calcular("22")[2], 22, "Maximo con un Numero")

    # Iteracion 3
    def test_calcular_maximo_dos_numero(self):
        self.assertEqual(Estadisticas().calcular("22,33")[2], 33, "Maximo con dos Numeros")

    # Iteracion 4
    def test_calcular_varios_numeros(self):
        self.assertEqual(Estadisticas().calcular("10, 12, 30")[2], 30, "Ciclo con varios numeros, Maximo con n Numeros, 1")
        self.assertEqual(Estadisticas().calcular("32, 12, 10")[2], 32, "Ciclo con varios numeros, Maximo con n Numeros, 2")
        self.assertEqual(Estadisticas().calcular("25, 30, 12")[2], 30, "Ciclo con varios numeros, Maximo con n Numeros, 3")
        self.assertEqual(Estadisticas().calcular("10, 12, 30, 45")[2], 45, "Ciclo con varios numeros, Maximo con n Numeros, 4")
        self.assertEqual(Estadisticas().calcular("70, 50, 10, 12")[2], 70, "Ciclo con varios numeros, Maximo con n Numeros, 5")
        self.assertEqual(Estadisticas().calcular("25, 50, 10, 12")[2], 50, "Ciclo con varios numeros, Maximo con n Numeros, 6")
        self.assertEqual(Estadisticas().calcular("25, 1, 55, 12")[2], 55, "Ciclo con varios numeros, Maximo con n Numeros, 7")

    #Paso 4 Devolver un arreglo con el numero de elementos y el minimo y el maximo, y el promedio

    #Iteracion 1
    def test_calcular_promedio(self):
        self.assertEqual(Estadisticas().calcular("")[3], 0, "String Vacio y Promedio")

    # Iteracion 2
    def test_calcular_un_numero(self):
       self.assertEqual(Estadisticas().calcular("13")[3], 13, "Promedio con un Numero")