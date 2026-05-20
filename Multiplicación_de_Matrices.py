def multiply_matrices(A, B):
    if len(A[0]) != len(B):
        raise ValueError("El número de columnas de A debe ser igual al número de filas de B")

    # Inicializar la matriz resultante con ceros
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    # Realizar la multiplicación de matrices
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result
# Ejemplo
A = [[1, 2, 3], [4, 5, 6]]
B = [[7, 8], [9, 10], [11, 12]]
result = multiply_matrices(A, B)
print(result)