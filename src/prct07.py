#!/usr/bin/python
#!encoding: UTF-8
import Ejer_Pi


valores = (10,100,1000,10000,100000,1000000,10000000,100000000)
for valor in valores:
  y = Ejer_Pi.aproximacion_pi(valor)
  print valor, y
  
  
# los numero de longitud superiores a 100.000.000, osea, superiores a 9 cifras pruducen un fallo en la memoria

# La notación científica falla porque yo tengo puesto que los valores deben ser enteros, no flotantes

# Archivo que se te crea para enlazar el programa principal con el módulo.