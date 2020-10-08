def multiply(x,y):
    return x*y

result=multiply(2,3)
print(result)

doubleNumber=lambda x,y: x*y

print(doubleNumber(2,3))

def quadratic(a,b,c):
    return lambda x: a*x**2+b*x+c

quadresult=quadratic(2,3,5)

print(quadresult(3))

number_list=[1,2,3,4,5,6,5,6,7,3,9,0,10,23,2,34,56]
evenNumberList=list(filter(lambda x:(x%2!=0),number_list))
print(evenNumberList)