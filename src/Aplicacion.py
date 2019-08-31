'''
Realizado por Jose Ramos
Fecha: 31 Agosto 2019
Correo: joselowolf@gmail.com
'''

from Analizar import *
import fileinput

for linea in fileinput.input("../datos/ejemplo1.txt"):
    strLinea=linea[:-1]
    print strLinea
    try:
        str_return = funAnalizarTexto(strLinea)
        if str_return:
            print str_return
    except:
        print "I have no idea what you are talking about"
    