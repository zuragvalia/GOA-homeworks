num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

numbers
if num1 < num2:
    smallest = num1
    largest = num2
else:
    smallest = num2
    largest = num1

using a for loop
print("All numbers from {smallest} to {largest}:")
for num in range(smallest, largest + 1):
    print(num, end=" ")  # Print each number followed by a space


print()