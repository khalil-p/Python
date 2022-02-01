# sum(n) = n+sum(n-1)

def sum_natural(n):
    if n == 0:
        return n
    else:
        return (n+(sum_natural(n-1)))


sum = sum_natural(2)
print(sum)
