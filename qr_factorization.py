import numpy as np

def householder(A):
    """
    Perform Householder transformation on a given vector A.

    inputs
    ------
    A: an input vector

    outputs
    -------
    v: a Householder vector
    tau: a scalar
    """
    alpha = A[0]
    s = np.power(np.linalg.norm(A[1:]), 2)
    v = A.copy()

    if s == 0:
        tau = 0
    else:
        t = np.sqrt(alpha**2 + s)
        if alpha <= 0:
            v[0] = alpha - t
        else:
            v[0] = -s / (alpha + t)
        numerator = v[0]**2
        denominator = s + v[0]**2
        tau = numerator / denominator
        v /= v[0]
    return v, tau


def qr_factorization(A):
    """
    Compute the QR factorization of a matrix A.

    inputs
    ------
    A: an input matrix with size m x n

    outputs
    -------
    Q: an orthonormal matrix with size m x n
    R: an upper triangular matrix with size n x n
    """
    row, col = A.shape
    R = A.copy()
    Q = np.identity(row)

    for j in range(0, col):
        # Use Householder Transformation
        v, tau = householder(R[j:, j])
        H = np.identity(row)
        H[j:, j:] -= tau * v.reshape(-1, 1) @ v
        R = H @ R
        Q = H @ Q
    return Q[:, :col], R[:col]


m = 4
n = 3
A = np.random.rand(4, 3)

q, r = np.linalg.qr(A)
Q, R = qr_factorization(A)

print("Q:\n", Q)
print("q:\n", q)
print("R:\n", R)
print("r:\n", r)

#Time Complexity: complexity is 2mn^2 − (2/3)n^3 flops -> O(n^3)
#Householder transform implementation to be used in QR Factorization
