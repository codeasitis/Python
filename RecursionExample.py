def factorial(n):
    if n==0 | n==1:
        return 1
    return n*factorial(n-1)


print(factorial(3))

def fabonacci(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    elif n>2:
        return fabonacci(n-1)+fabonacci(n-2)


for x in range(1,10):
    print(x,"",fabonacci(x))

