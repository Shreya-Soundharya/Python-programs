#Matrix Multiplication

def matrix_multiply(matrix1, matrix2):
    # Check if the matrices are compatible for multiplication
    if len(matrix1[0]) != len(matrix2):
        return None  # Matrices are not compatible

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    # Perform matrix multiplication
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

def get_matrix_input(prompt):
    try:
        rows = int(input(prompt + " Enter the number of rows: "))
        cols = int(input(prompt + " Enter the number of columns: "))
        matrix = []
        print(f"Enter {rows} rows with {cols} values separated by spaces:")
        for _ in range(rows):
            row = [int(x) for x in input().split()]
            if len(row) != cols:
                raise ValueError("Invalid input. Number of columns must match the specified value.")
            matrix.append(row)
        return matrix
    except ValueError as e:
        print(e)
        return None

print("Matrix 1:")
matrix1 = get_matrix_input("For matrix 1")

print("Matrix 2:")
matrix2 = get_matrix_input("For matrix 2")

if matrix1 is not None and matrix2 is not None:
    result = matrix_multiply(matrix1, matrix2)

if result is None:
    print("Matrix multiplication is not possible. The number of columns in matrix 1 must match the number of rows in matrix 2.")

else:
    print("Matrix multiplication result:")
    for row in result:
        print(" ".join(map(str, row)))
