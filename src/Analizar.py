'''
Realizado por Jose Ramos
Fecha: 31 Agosto 2019
Correo: joselowolf@gmail.com
'''

from Romanos import castRomanoToDecial

# Recolenca las referencias entre palabras y numeros romanos.
referencias = {}

# Se define el dominio de simbolos romanos ....
DominioRomano=['I','V','X','L','C','D','M']
#Se almacena las condiciones adicionales los valores de silver, gold y Iron
CondicionesAdicionales = {}
def funAnalizarTexto(linea):

    if linea[-1] in DominioRomano:
        '''
        Recolecta los referencias a los romanos
        se distinguen porque al final de linea es un numero romano
        glob = I
        prok = v
        pish = X
        tegj = L
        Almancena en el dicionario.
        '''
        palabras = linea.split(' ')
        # glob = I
        referencias[palabras[0]] = palabras[2]
        return
    
    elif linea[-1] == 's':
        '''
        Analiza los datos ls condiciones adicionales se distinguen porque termina con s
        glob glob Silver is 34 Credits
        glob prok Gold is 57800 Credits
        pish pish Iron is 3910 Credits
        '''
        palabras = linea.split(' ') # separa en palabras
        aux = ''

        # busca todas las refencionas hasta que encuentre las palabras Silver, Gold o Iron
        for palabra in palabras:
            if (palabra == 'Silver') or (palabra == 'Gold') or (palabra == 'Iron'):
                break
            else:
                aux += referencias[palabra]
        
        aux =  castRomanoToDecial(aux)
        valor = int(palabras[-2])/int(aux)
        # Silver = 17
        # Gold = 14450
        # Iron = 195
        CondicionesAdicionales[palabras[-4]] = valor
        return
    
    elif linea[-1] == '?':
        '''
        Se reponde las preguntas se identifica por ?
        hay dos tipos de preguntas much o many.
        '''
        palabras = linea.split(' ') # se separa en palablas la linea
        if  palabras[1] == 'much': 
            aux1 = ''
            aux2 = ''
            for i in range(3,len(palabras)-1):
                aux2 += palabras[i]+' '
                aux1 += referencias[palabras[i]]
            
            # se calcula en romandos enviado aux que es igual a las palabras encontradas
            return aux2+"is "+str(castRomanoToDecial(aux1))
        
        elif palabras[1] == 'many':
            aux2 = ''
            aux1 = ''
            for i in range(4,len(palabras)-2):
                aux1 += palabras[i]+' '
                aux2 += referencias[palabras[i]]
            
            return aux1+palabras[-2]+' is '+ str(CondicionesAdicionales[palabras[-2]]*castRomanoToDecial(aux2) )+ ' Credits'