def Division(a,b):
    if (b<=0):
        raise TypeError("number must be greater than 0")
    return a/b


try:
    result=Division(12,0)
    print(result)
except (ZeroDivisionError, SyntaxError, ValueError):
    print("Zero Division caught")
except TypeError:
    print("Type error is caught")
except :
    print("Generic Exception is caught")
else:
    print("else block executed")
finally:
    print("finally block executed")
