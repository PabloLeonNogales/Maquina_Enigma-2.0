# Definitivamente, vamos a unir el engranaje de rotores al reflector, para generar la máquina enigma. 
# Por esta razón, llamo a este archivo main.py

# En caso de trabajar con una ventana gráfica n vez de con consola, este sería el archivo de gestión de gráficos.

from ClassRotor import *
from ClassReflector import *
from piezas import *

class Enigma():

    rotores = []

    def __init__(self, reflector, rotores, enigma_ini = None):
    
        self.reflector = Reflector()
        self.enigma_ini = enigma_ini
        for i in range (len(rotores)):
            rotor = Rotor(rotor = rotores[i])
            if enigma_ini != None:
                rotor.pos_ini(enigma_ini[i])
            self.rotores.append(rotor)
        self.abecedario = self.rotores[0].abecedario
    
    def enigmaCodifica(self, letra):
        pin_entrada = self.abecedario.index(letra)
        _salta = True
        for rotor in self.rotores:
            if _salta:
                _salta = rotor.avanza()
            pin_entrada = rotor.codifica(pin_entrada)
        pin_salida = self.reflector.refleja(pin_entrada)
        for rotor in self.rotores[::-1]:
            pin_salida = rotor.decodifica(pin_salida)
        return self.abecedario[pin_salida]
    

if __name__ == '__main__':

    enigma = Enigma('B',('I', 'II'), 'OA')

    letra = 'NSWX'
    salida = ""
#    letra = input('¿Qué letra o frase (sin espacios) quieres pulsar? ')
    for n in letra:
        salida = salida + enigma.enigmaCodifica(n)
        
    print (salida)
