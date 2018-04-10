def mult(m, n):
    if m == 0 or n == 0:
        return 0
    if m == 1:
        return n
    if n == 1:
        return m
    
    return m + mult(m, n - 1)

def multLoop(m, n):
    x = 0
    i = 0
    while i < n:
        x += m
        i += 1
    return x