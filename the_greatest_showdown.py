#Task 1 and Task 2 - Find the smallest and largest of 3 numbers

num1 = int(input("Please enter a number.\n"))
num2 = int(input("Please enter a number.\n"))
num3= int(input("Please enter a number.\n"))

lst = [num1, num2, num3]
print(f"The smallest number is {min(lst)}. The largest number is {max(lst)}.")
