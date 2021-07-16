import pyodbc

conn=pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=localhost;"
    "Database=Dummy;"
    "Trusted_connection=yes;"
)

cursor=conn.cursor()
cursor.execute("insert into Employee(Name,Age) values (?,?)",('CodeAsItis',35))
conn.commit();



cursor.execute("Update Employee set Age=39 where Id=6")
conn.commit();


cursor.execute("Delete from Employee  where Id=(?)",(6))
conn.commit();

cursor.execute('Select * From Employee')
for row in cursor:
    print(f'row={row}')

print();