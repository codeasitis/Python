# Variable - 
# name 
x1=5
def firstFun():
    global x
    x=4
    print(x)
def secondFun():
    print(x)
firstFun()
secondFun()
print(x)