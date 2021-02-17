# Definición de Rotores y Reflectores Fijos. Al final, optaremos por esta opción para evitar 
# que los randoms nosmolesten a la hora de hacer pruebas. En todo caso, 
# podremos volver a los randoms cuando queramos

# Para los rotores y reflectores ingleses, uso el ejemplo gráfico de la máquina en el paquete de Pringles.

from random import *

#-----------------------------------------------
#                DICCIONARIOS
# ----------------------------------------------

ENGLISHDIC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
             #EKMFLGDQVZNTOWYHXUSPAIBRCJ
ESPANOLDIC = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

#-----------------------------------------------
# ROTORES (DICCIONARIO INGLÉS, 
# ORIGINALES DE LA MÁQUINA ALEMANA)
#-----------------------------------------------

rotor_types = {
    "I":     ("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q"),
    "II":    ("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E"),
    "III":   ("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V"),
    "IV":    ("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J"),
    "V":     ("VZBRGITYUPSDNHLXAWMJQOFECK", "Z"),
    "VI":    ("JPGVOUMFYQBENHZRDKASXLICTW", "ZM"),
    "VII":   ("NZJHGRCXMYSWBOUFAIVLPEKQDT", "ZM"),
    "VIII":  ("FKQHTLXOCBJSPDZRAMEWNIUYGV", "ZM"),
    "BETA":  ("LEYJVCNIXWPBQMDRTAKZGFUHOS", "A"),
    "GAMMA": ("FSOKANUERHMBTIYCWLQPZXVGJD", "A")
}

# --------------------------------------------
# REFLECTORES (DICCIONARIO INGLÉS, 
# ORIGINALES DE LA MÁQUINA ALEMANA)
# --------------------------------------------

reflector_types= {
    'B':     ["ABCDEFGHIJKLMNOPQRSTUVWXYZ", "YRUHQSLDPXNGOKMIEBFZCWVJAT"],
    'C':     ["ABCDEFGHIJKLMNOPQRSTUVWXYZ", "FVPJIAOYEDRZXWGCTKUQSBNMHL"],
    'D':     ["ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ZXWVUTSRQYPONMLKIHGFEDCBJA"],
    'Bfine': ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ENKQAUYWJICOPBLMDXZVFTHRGS'],
    'Cfine': ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'RDOBJNTKVEHMLFCWZAXGYIPSUQ']
}

# También definiremos los generadores de rotores y reflectores, digamos que son las 'fábricas' que producen 
# esas piezas. Por si algún día queremos cambiar las especificaciones de los que tenemos, o crear nuevos a 
# partir de otros diccionarios... Son funciones, no clases. En realidad deberáin estar en sus respectivas 
# clases, pero lo coloco aquí para no ensuciar mucho el código que importa. 
 
def rotorAleatorio(abecedario = ENGLISHDIC):
    abecedario = abecedario
    rotor = [n for n in range(len(abecedario))]
    shuffle(rotor)
    print('Rotor aleatorio para el diccionario {}: {}'.format(abecedario, rotor))    

def reflectorAleatorio(abecedario = ENGLISHDIC):
    abecedario = abecedario
    reflector = []
    num = [n for n in range(len(abecedario))]
    #Generamos el reflector desordenado
    while len(num) > 1:
        n = randint(1,len(num)-1)
        reflector.append((num[0],num[n]))
        reflector.append((num[n],num[0]))
        num.pop(n)
        num.pop(0)
    if len(num) == 1:
        reflector.append((num[0],num[0]))
    # Ordenamos el reflector
    reflector = sorted(reflector)
    print('Reflector aleatorio para el diccionario {}: {}'.format(abecedario, reflector))  

if __name__ == '__main__':
    
    rotorAleatorio()
    reflectorAleatorio()
    
