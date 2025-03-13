def contar_cubos(n):
    total_cubos = n ** 3
    cubos_internos = (n - 2) ** 3 if n > 2 else 0
    cubos_1_cara = 6 * (n - 2) ** 2 if n > 2 else 0
    cubos_2_caras = 12 * (n - 2) if n > 2 else 0
    cubos_3_caras = 8
    cubos_mas_4_caras = 0  # Si el cubo grande cuanta, seria 1

    return {
        "Total de cubos": total_cubos,
        "Cubos internos (0 caras)": cubos_internos,
        "Cubos con 1 cara visible": cubos_1_cara,
        "Cubos con 2 caras visibles": cubos_2_caras,
        "Cubos con 3 caras visibles": cubos_3_caras,
        "Cubos con más de 4 caras": cubos_mas_4_caras
    }

# Ejemplo con un cubo de 4x4x4 como en el problema planteado
resultado = contar_cubos(4)

for key, value in resultado.items():
    print(f"{key}: {value}")
