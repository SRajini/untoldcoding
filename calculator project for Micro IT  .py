a=int(input("enter the num1:"))
b=int(input("enter the num2:"))
choice=int(input("enter the choice:"))
if choice == 1:
  print("addition of two numbers:",a+b)
elif choice == 2:
  print("subtraction of two numbers:",a-b)
elif choice == 3:
  print("multiplication of two numbers:",a*b)
elif choice == 4:
  print("division of two numbers:", a/b)
else:
  print("not a calculator")