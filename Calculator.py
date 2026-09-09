print('''it's only for input number like : 1,2 , ...
then please don't use float numbers like: 1.1 , 2.5''')
first_number = input("first_number:")
second_number = input("second_number:")
Mathematical_operation = input("Mathematical_operation:")
if Mathematical_operation == "+" :
    print(int(first_number) + int(second_number))
elif Mathematical_operation == "-":
    print(int(first_number) - int(second_number))
elif Mathematical_operation == "*":
    print(int(first_number) * int(second_number))
elif Mathematical_operation == "/":
    print(int(first_number) / int(second_number))
elif Mathematical_operation == "**":
    print(int(first_number) ** int(second_number))
elif Mathematical_operation == "//":
    print(int(first_number) // int(second_number))
else:
    print(''' it's not Mathematical_operation''')



