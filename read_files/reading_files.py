# w - write     r - read    a - append (can't modify info but can add)  r+ - read&write

employee_file = open("/Volumes/Terabyte/Programming/mikros_pythonas/read_files/employees.txt", "r")
for employee in employee_file.readlines():
    print(employee)

employee_file.close()