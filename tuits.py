import math

def calcular_bits_tuit(caracteres_posibles, limite_caracteres_tuit):
    bits_por_caracter = math.ceil(math.log2(caracteres_posibles))
    
    capacidad_tuit = limite_caracteres_tuit

    bits_tuit_total = bits_por_caracter * limite_caracteres_tuit
    
    return bits_por_caracter, capacidad_tuit, bits_tuit_total

bits_caracter, capacidad, bits_total = calcular_bits_tuit(100, 100) 
# Más acertado es poner como capacidad 280, pero siguiendo el problema es 100 

print(f"Bits por carácter: {bits_caracter}")
print(f"Capacidad del tuit (caracteres): {capacidad}")
print(f"Bits totales para el tuit: {bits_total}")