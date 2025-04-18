import math

# Diccionario de los simbolos de la clase
simbolos = {
    'A' = 0.2,
    'B' = 0.1,
    'Esc' = 0.1,
    '#' = 0.1,
    'H' = 0.1,
    'O' = 0.1,
    'L' = 0.1,
    '1' = 0.1,
    '*' = 0.1
}

# Respectiva representación en binario
codigos_binarios = {
    'A': '01000111',
    'B': '11100011',
    'Esc': '11100000',
    '#': '01110110',
    'H': '01011111',
    'O': '10000011',
    'L': '11100001',
    '1': '01011111',
    '*': '11110000'
}

# Funcion para calcular entropía total
def calcular_entropia(simbolos):
    entropia_total = 0
    for prob in simbolos.values():
        if prob > 0:
            entropia_total = entropia_total + (prob * math.log2(1 / prob))
    return entropia_total

# Funcion para codificar cualquier mensaje
def codificar_mensaje(mensaje, codigos_binarios):
    binario = ''
    for letra in mensaje:
        if letra in codigos_binarios:
            binario = binario + codigos_binarios[letra]
        else:
            print(f"Simbolo '{letra}' no tiene código definido.")
    return binario

# Función principal 
def analizar_mensaje(mensaje):
    print(f"\nMensaje: '{mensaje}'")
    mensaje = mensaje.upper()
    mensaje_codificado = codificar_mensaje(mensaje, codigos_binarios)
    bits_totales = len(mensaje_codificado)
    entropia_total = calcular_entropia(simbolos)
    entropia_esperada = entropia_total * len(mensaje)

    print(f"Bits usados (código binario real): {bits_totales}")
    print(f"Entropía total por símbolo: {entropia_total:.3f} bits")
    print(f"Entropía esperada para el mensaje: {entropia_esperada:.3f} bits")
    print(f"Código binario del mensaje: {mensaje_codificado}")

# Aqui pruebo con el mensaje HOLA, se puede cualquier palabra que tenga las palabras del diccionario 
analizar_mensaje("HOLA")