from piezas import *

class Reflector():

    def __init__(self, abecedario = ENGLISHDIC, reflector = 'B'):
        self.abecedario = abecedario
        self.reflector = reflector_types[reflector][1]

    def __str__(self):
        return 'Reflector' 

    # Función que refleja una posición (de P0 a P1). Notar que, como el reflector
    # está ordenado, se elige el par que ocupa la posición 'posicion' y devuelve su reflejo.
    # Hay que acordarse de cómo definir esta posición en la máquina (ahora mismo, 
    # la posición 4 es, por ejemplo, el par quinto, por la nomenclatura de Python).
    def refleja(self, pin_entrada):
        reflejo = self.reflector[pin_entrada]
        pin_salida = self.abecedario.index(reflejo)
        return pin_salida

if __name__ == '__main__':

    s = Reflector()
    print(s.reflector)
    print(s.refleja(16))