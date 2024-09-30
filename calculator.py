num1 = int(input("Enter First number: "))
num2 = int(input("Enter Second number: "))

choice = input("Enter the operation: (Options + , - , * , / , %)")

if choice == "+":
 sum_of_num = num1 + num2
 print("addition: ",sum_of_num)

elif choice == "-":
 diff_of_num = num1 - num2
 print("subtraction: ",diff_of_num)

elif choice == "*":
 prod_of_num = num1 * num2
 print("multiplication: ",prod_of_num)

elif choice == "/":
  div_of_num = num1 / num2
  print("division: ",div_of_num)

elif choice == "%":
 rem_of_num = num1 % num2
 print("remainder: ",rem_of_num)
else:
  print("Invalid choice")