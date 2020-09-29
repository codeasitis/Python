dict_employee={"Mohan":23,"Sohan":32,"Rohan":45}
print(dict_employee["Sohan"])
print(dict_employee.get("Sohan"))
dict_employee["Sohan"]=35
print(dict_employee)
del(dict_employee["Rohan"])
print(dict_employee)
print("Rohan" in dict_employee)
print(dict_employee.keys())
print(dict_employee.values())
print(dict_employee.items())

# nested dictionary
employee1={"Name":"Mohan"}
employee2={"Name":"Rohan"}
employee3={"Name":"Sohan"}
employee_dict={"emp1":employee2,"emp2":employee1}
print(employee_dict)