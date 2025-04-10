## Algoritmo de cubos basado en las siguientes ecuaciones

- Total de cubos: 4^3 = 64

- Cubos internos (0 caras): (4-2)^3 = 8

- Cubos con 1 cara: 6x(4-2)^2 = 24

- Cubos con 2 caras: 12×(4−2)= 24

- Cubos con 3 caras: 8

- Cubos con más de 4 caras: 0 (si el cubo grande cuenta sería 1)

---

## Calcular bits por carácter:

- log2(100) ≈ 6.644 bits. Como no podemos usar fracciones de bits, redondeamos hacia arriba a 7 bits (esto se llama "techo" o ceil).

- Si el límite es 100 caracteres, la capacidad es 100 caracteres.
  7 bits/carácter \* 100 caracteres = 700 bits.
