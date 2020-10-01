# Conditional Statement - If, elif , else , Nested If
age=13;
if age>=60:
    if age>70:
        print("You are now 70")
    print("YOu are senior citizen")
elif age>18 and age<60:
    print("you are adult")
else:
    print("you are younger")

print("you are adult") if age>=18 else print("you are younger")