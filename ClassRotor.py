from piezas import *

class Rotor():

    def __init__(self, abecedario = ENGLISHDIC, rotor = 'I', pos_ini = None):
        
        self.abecedario = abecedario
        self.rotor = rotor_types[rotor][0]
        self.nombre_rotor = rotor

        if pos_ini == None:
            self.__pos_ini = self.abecedario[0]
            self.__num_pos_ini = 0
        else:
            self.__pos_ini = pos_ini
            self.__num_pos_ini = list(self.abecedario).index(pos_ini)
        
        self.salto = rotor_types[rotor][1]

    def __str__(self):
        return 'Rotor ' + self.nombre_rotor

    def pos_ini(self, value = None):
        if value == None:
            return self.__pos_ini
        else:
            self.__pos_ini = value
            self.__num_pos_ini = list(self.abecedario).index(self.__pos_ini)

    # Cuando presionamos una tecla, el rotor avanza una posición. 
    # Esta función hace precisamente eso.
    def avanza(self):
        self.__num_pos_ini = (self.__num_pos_ini + 1) % len(self.abecedario)
        self.__pos_ini = self.abecedario[self.__num_pos_ini]
        return self.__pos_ini in self.salto

    # Proceso (método) de codificación
    def codifica(self,pin_derecho):
        pin_total = pin_derecho + self.__num_pos_ini
        letra_izquierda = self.rotor[pin_total % len(self.abecedario)]
        pin_izquierdo = (self.abecedario.index(letra_izquierda) - self.__num_pos_ini) % len(self.abecedario)
        return pin_izquierdo

    # Proceso (método) de decodificación)
    def decodifica(self,pin_izquierdo):
        pin_total = pin_izquierdo + self.__num_pos_ini   
        letra_izquierda = self.abecedario[pin_total % len(self.abecedario)]
        pin_derecho = (self.rotor.index(letra_izquierda) - self.__num_pos_ini) % len(self.abecedario)
        return pin_derecho


if __name__ == '__main__':
    
    r = Rotor()
