def lcs_dc(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m-1] == Y[n-1]:
        return 1 + lcs_dc(X, Y, m, n-1)
    else:
        return max(lcs_dc(X, Y, m, n-1), lcs_dc(X, Y, m-1, n))


def lcs_dp(X, Y):
    m = len(X)
    n = len(Y)
    L = [[None]*(n+1) for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    
    for i in range(m+1):
        print(L[i])
    print("LCS = ", lcs_dp_traceback(X, Y, L))

    return L[m][n]

def lcs_dp_traceback(X, Y, L):
    lcs = ""
    i = len(X)
    j = len(Y)
    while i > 0 and j > 0:
        v = L[i][j]
        if v > L[i][j-1] and v > L[i-1][j] and v > L[i-1][j-1]:
            i -= 1
            j -= 1
            lcs = X[i] + lcs
        
        elif v == L[i][j-1] and v > L[i-1][j]: j -= 1
        else : i -= 1
    return lcs
X = "Game Over"
Y = "Hello World"
print("X = ", X)
print("Y = ", Y)
print("LCS", lcs_dc(X, Y, len(X), len(Y)))
print("LCS", lcs_dp(X, Y) )


def edit_distance_dp(S, T, m, n):
    E = [[0 * (n+1)] for _ in range(m+1)]
    for i in range(m+1):
        E[i][0] = 1
    for j in range(n+1):
        E[0][j] = j
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if S[i] == T[j]: a = 0
            else: a = 1
            E[i][j] = min(E[i-1][j] + 1, E[i][j-1] +1, E[i-1][j-1]+a)
        
    return E[m][n]

S = "tuesday"
T = "thursday"
m = len(S)
n = len(T)
print("munjayol: ", S, T)
print("pyonjipkori= ", edit_distance_dp(S, T, m, n))