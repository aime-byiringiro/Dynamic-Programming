"""
A is p * q , B is q * r, and C is p * r
"""
def rectangular_matrix_multiply(A, B, C, p, q, r):
    for i in range(p):
        for j in range(r):
            for k in range(q):
                C[i][j] = C[i][j] + A[i][k] * B[k][j]
