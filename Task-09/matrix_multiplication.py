import time


# -------------------- Naive Matrix Multiplication --------------------

def naive_multiply(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result


# -------------------- Matrix Addition --------------------

def add_matrices(A, B):
    rows = len(A)
    cols = len(A[0])

    return [
        [A[i][j] + B[i][j] for j in range(cols)]
        for i in range(rows)
    ]


# -------------------- Matrix Subtraction --------------------

def subtract_matrices(A, B):
    rows = len(A)
    cols = len(A[0])

    return [
        [A[i][j] - B[i][j] for j in range(cols)]
        for i in range(rows)
    ]


# -------------------- Divide and Conquer --------------------

def divide_and_conquer(A, B):
    n = len(A)

    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2

    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    C11 = add_matrices(
        divide_and_conquer(A11, B11),
        divide_and_conquer(A12, B21)
    )

    C12 = add_matrices(
        divide_and_conquer(A11, B12),
        divide_and_conquer(A12, B22)
    )

    C21 = add_matrices(
        divide_and_conquer(A21, B11),
        divide_and_conquer(A22, B21)
    )

    C22 = add_matrices(
        divide_and_conquer(A21, B12),
        divide_and_conquer(A22, B22)
    )

    top = [C11[i] + C12[i] for i in range(mid)]
    bottom = [C21[i] + C22[i] for i in range(mid)]

    return top + bottom


# -------------------- Strassen's Algorithm --------------------

def strassen_multiply(A, B):
    n = len(A)

    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2

    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    M1 = strassen_multiply(
        add_matrices(A11, A22),
        add_matrices(B11, B22)
    )

    M2 = strassen_multiply(
        add_matrices(A21, A22),
        B11
    )

    M3 = strassen_multiply(
        A11,
        subtract_matrices(B12, B22)
    )

    M4 = strassen_multiply(
        A22,
        subtract_matrices(B21, B11)
    )

    M5 = strassen_multiply(
        add_matrices(A11, A12),
        B22
    )

    M6 = strassen_multiply(
        subtract_matrices(A21, A11),
        add_matrices(B11, B12)
    )

    M7 = strassen_multiply(
        subtract_matrices(A12, A22),
        add_matrices(B21, B22)
    )

    C11 = add_matrices(
        subtract_matrices(
            add_matrices(M1, M4),
            M5
        ),
        M7
    )

    C12 = add_matrices(M3, M5)

    C21 = add_matrices(M2, M4)

    C22 = add_matrices(
        subtract_matrices(
            add_matrices(M1, M3),
            M2
        ),
        M6
    )

    top = [C11[i] + C12[i] for i in range(mid)]
    bottom = [C21[i] + C22[i] for i in range(mid)]

    return top + bottom


# -------------------- Input Matrix --------------------

def read_matrix(rows, cols):
    matrix = []

    print(f"Enter the {rows} x {cols} matrix row by row:")

    for i in range(rows):
        while True:
            row = list(map(int, input(f"Row {i + 1}: ").split()))

            if len(row) == cols:
                matrix.append(row)
                break

            print(f"Please enter exactly {cols} numbers.")

    return matrix


# -------------------- Padding --------------------

def pad_matrix(matrix, size):
    rows = len(matrix)
    cols = len(matrix[0])

    padded = [[0] * size for _ in range(size)]

    for i in range(rows):
        for j in range(cols):
            padded[i][j] = matrix[i][j]

    return padded


def remove_padding(matrix, rows, cols):
    return [row[:cols] for row in matrix[:rows]]


# -------------------- Print Matrix --------------------

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


# -------------------- Main Program --------------------

def main():
    print("=== Matrix Multiplication Showdown ===")

    rows_A = int(input("Enter number of rows in Matrix A: "))
    cols_A = int(input("Enter number of columns in Matrix A: "))

    rows_B = int(input("Enter number of rows in Matrix B: "))
    cols_B = int(input("Enter number of columns in Matrix B: "))

    if cols_A != rows_B:
        print("Matrix multiplication is not possible.")
        print("Columns of A must equal rows of B.")
        return

    A = read_matrix(rows_A, cols_A)
    B = read_matrix(rows_B, cols_B)

    result_rows = rows_A
    result_cols = cols_B

    # Find the next power of 2
    size = 1

    while size < max(rows_A, cols_A, rows_B, cols_B):
        size *= 2

    A_padded = pad_matrix(A, size)
    B_padded = pad_matrix(B, size)

    # -------------------- Naive --------------------

    start = time.perf_counter()

    result_naive = naive_multiply(A, B)

    naive_time = time.perf_counter() - start

    # -------------------- Divide and Conquer --------------------

    start = time.perf_counter()

    result_dc = divide_and_conquer(A_padded, B_padded)

    dc_time = time.perf_counter() - start

    result_dc = remove_padding(
        result_dc,
        result_rows,
        result_cols
    )

    # -------------------- Strassen --------------------

    start = time.perf_counter()

    result_strassen = strassen_multiply(
        A_padded,
        B_padded
    )

    strassen_time = time.perf_counter() - start

    result_strassen = remove_padding(
        result_strassen,
        result_rows,
        result_cols
    )

    # -------------------- Verification --------------------

    results_match = (
        result_naive == result_dc == result_strassen
    )

    # -------------------- Display Results --------------------

    print("\n=== Matrix A ===")
    print_matrix(A)

    print("\n=== Matrix B ===")
    print_matrix(B)

    print("\n=== Result ===")
    print_matrix(result_naive)

    print("\n=== Execution Time ===")

    print(f"Naive:            {naive_time:.8f} seconds")
    print(f"Divide & Conquer: {dc_time:.8f} seconds")
    print(f"Strassen:         {strassen_time:.8f} seconds")

    print("\n=== Verification ===")

    if results_match:
        print("All three algorithms produced the same result.")
    else:
        print("ERROR: Results do not match.")


# -------------------- Run Program --------------------

if __name__ == "__main__":
    main()