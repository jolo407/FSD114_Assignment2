def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)

n=5,6,7,8
fact(n)