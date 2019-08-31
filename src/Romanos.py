'''
Realizado por Jose Ramos
Fecha: 31 Agosto 2019
Correo: joselowolf@gmail.com
'''
import re

def castRomanoToDecial(NumRomano):
    '''
    Convierte numeros romanos a decimales
    utiliza expresiones reguales para validar el numero
    '''
    if re.search('^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$',NumRomano)!=None:
        NumDecimal = {"patron":"","valor":0}
        EquivalenciaRomanos = {
            "0":('','','','M'),             #          1000
            "1":('CM','CD','D','C',100), #900 400 500 100
            "2":('XC','XL','L','X',10), #90 40 50 10
            "3":('IX','IV','V','I',1)#9 4 5 1
            }
        i = 3
        equalRomanos = sorted(EquivalenciaRomanos.items())

        for SecRomando in equalRomanos:
            if SecRomando[0] != '0':
                patronSeccion = NumDecimal["patron"].join(['',SecRomando[1][0]])
                if re.search(patronSeccion,NumRomano) != None:
                    NumDecimal["valor"] += 9*SecRomando[1][4]
                    NumDecimal["patron"] = patronSeccion
                else:
                    patronSeccion = NumDecimal["patron"].join(['',SecRomando[1][1]])
                    if re.search(patronSeccion,NumRomano) != None:
                        NumDecimal["valor"] += 4*SecRomando[1][4]
                        NumDecimal["patron"] = patronSeccion
                    else:
                        patronSeccion = NumDecimal["patron"].join(['',SecRomando[1][2]])
                        if re.search(patronSeccion,NumRomano) != None:
                            NumDecimal["valor"] += 5*SecRomando[1][4]
                            NumDecimal["patron"] = patronSeccion
            
            if NumDecimal["patron"] == '':
                NumDecimal["patron"] = '^'
            aux = ''
            suma = 0
            '''
            Calcula el total de todas las secciones de los romanos
            '''
            for v in range(0,4):
                aux1 = SecRomando[1][3].join(['','{']).join(['',str(v)]).join(['','}'])
                patronSeccion = NumDecimal["patron"].join(['',aux1])
                if re.search(patronSeccion,NumRomano) != None:
                    suma = v*(10**i)
                    aux = patronSeccion
            if aux <> '':
                NumDecimal["patron"] = aux
            else:
                NumDecimal["patron"] = patronSeccion
            NumDecimal['valor'] += suma
            i -= 1
        
        return NumDecimal['valor']
    else:
        print 'this is not a numer valid'

    
