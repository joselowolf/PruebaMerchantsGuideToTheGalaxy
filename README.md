# PruebaMerchantsGuideToTheGalaxy
Desarrollo por José Ramos
Correo: joselowolf@gmail.com
## Tarea
You decided to give up on earth after the latest financial collapse left 99.99% of the earth's population with 0.01% of the wealth. Luckily, with the scant sum of money that is left in your account, you are able to afford to rent a spaceship, leave earth, and fly all over the galaxy to sell common metals and dirt (which apparently is worth a lot).Buying and selling over the galaxy requires you to convert numbers and units, and you decided to write a program to help you.The numbers used for intergalactic transactions follows similar convention to the roman numerals and you have painstakingly collected the appropriate translation between them.Roman numerals are based on seven symbols:

SymbolValue

- I 1
- V 5
- X 10
- L 250
- C 100
- D 500
- M 1,000

Numbers are formed by combining symbols together and adding the values. For example, MMVI is 1000 + 1000 + 5 + 1 = 2006. Generally, symbols are placed in order of value, starting with the largest values. When smaller values precede larger values, the smaller values are subtracted from the larger values, and the result is added to the total. For example MCMXLIV = 1000 + (1000 - 100) + (50 - 10) + (5 - 1) = 1944.
The symbols "I", "X", "C", and "M" can be repeated three times in succession, but no more. (They may appear four times if the third and fourth are separated by a smaller value, such as XXXIX.) "D", "L", and "V" can never be repeated.

"I" can be subtracted from "V" and "X" only. "X" can be subtracted from "L" and "C" only. "C" can be subtracted from "D" and "M" only. "V", "L", and "D" can never be subtracted.
Only one small-value symbol may be subtracted from any large-value symbol.

A number written in Arabic numerals can be broken into digits. For example, 1903 is composed of 1, 9, 0, and 3. To write the Roman numeral, each of the non-zero digits should be treated separately. In the above example, 1,000 = M, 900 = CM, and 3 = III. Therefore, 1903 = MCMIII.
-- Source: Wikipedia (http://en.wikipedia.org/wiki/Roman_numerals)Input to your program consists of lines of text detailing your notes on the conversion between intergalactic units and roman numerals. You are expected to handle invalid queries appropriately.

Test input:

glob is I
prok is V
pish is X
tegj is L
glob glob Silver is 34 Credits<
glob prok Gold is 57800 Credits
pish pish Iron is 3910 Credits
how much is pish tegj glob glob ?
how many Credits is glob prok Silver ?
how many Credits is glob prok Gold ?
how many Credits is glob prok Iron ?
how much wood could a woodchuck chuck if a woodchuck could chuck wood ?


Test Output:<br />
pish tegj glob glob is 42<br />
glob prok Silver is 68 Credits<br />
glob prok Gold is 57800 Credits<br />
glob prok Iron is 782 Credits<br />
I have no idea what you are talking about<br />

## Estrategia de desarrollo.

1. Se deberá realizar un algoritmo que permita convertir números romanos a decimal.
2. Se deberá detectar palabras equivalentes a números romanos ejemplo glob = I. Detectado el numero romano equivalente.
3. Se deberá detectar las condiciones adicionales ejemplo en valor de Silver, Gold, Iron. Con el caracter "s" al final 
4. Se debera detectar las preguntas con el caracter "?" al final.
    4.1 Detectar si es much o many.
    4.5 Calcular el valor.

5. Se desarrolloando pruebas unitarias automáticas que validen el funcionamiento.
6. Manual de usuario
##  Manual de usuario.

Los textos a analizar se encuentra en el archivo cat datos/ejemplo1.txt.
```sh
cat datos/ejemplo1.txt.
```

para ejecutar ingresar a la carpeta src y ejecutar:
```sh
cd src
python Aplicacion.py
```


**respuesta:**
```sh
glob is I
prok is V
pish is X
tegj is L
glob glob Silver is 34 Credits
glob prok Gold is 57800 Credits
pish pish Iron is 3910 Credits
how much is pish tegj glob glob ?
pish tegj glob glob is 42
how many Credits is glob prok Silver ?
glob prok Silver is 68 Credits
how many Credits is glob prok Gold ?
glob prok Gold is 57800 Credits
how many Credits is glob prok Iron ?
glob prok Iron is 780 Credits
how much wood could a woodchuck chuck if a woodchuck could chuck wood ?
I have no idea what you are talking about
```

Para ejecutar las pruebas automáticas en la carpeta del proyecto ejecutar
```sh
python -m unittest discover -v
```
**resultado:**
```sh
test_ejercicio1 (test_convertir_romandos.TestStringMethods) ... ok
test_ejercicio1903 (test_convertir_romandos.TestStringMethods) ... ok
test_ejercicio1944 (test_convertir_romandos.TestStringMethods) ... ok
test_ejercicio2 (test_convertir_romandos.TestStringMethods) ... ok
test_ejercicio2006 (test_convertir_romandos.TestStringMethods) ... ok
test_ejercicio39 (test_convertir_romandos.TestStringMethods) ... ok
test_ejercicio4 (test_convertir_romandos.TestStringMethods) ... ok
test_ejercicio5 (test_convertir_romandos.TestStringMethods) ... ok
test_ejercicio6 (test_convertir_romandos.TestStringMethods) ... ok
test_ejercicioERROR (test_convertir_romandos.TestStringMethods) ... this is not a numer valid
ok


----------------------------------------------------------------------
Ran 10 tests in 0.012s

OK
```

## Software desarrollo
Python 2.7.10
Microsof Visual Studio Code Versión: 1.37.1
Mac os Mojave Version 10.14.16.

La ejecucion en windows en las misma no deberia traer errores o problemas.