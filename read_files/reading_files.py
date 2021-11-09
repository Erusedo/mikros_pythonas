# w - write     r - read    a - append (can't modify info but can add)  r+ - read&write

employee_file = open("employees.txt", "r")

print(employee_file.readable())

employee_file.close()