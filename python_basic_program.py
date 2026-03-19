# 1. Print Hello World
print("Hello, World !")

# 2. Calculate the sum of two numbers
a = 5
b = 10
sum = a + b
print("The sum of", a, "and", b, "is", sum)

# Another way to calculate the sum of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a + b)

# 3. Find Largest of Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Largest number is:", a)
else:
    print("Largest number is:", b)

#Another way to find largest of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: ")) 
largest = max(a, b)
print("Largest number is:", largest)

# 4. Check if a number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is an even number.")    
else:
    print(num, "is an odd number.")

# another way to check if a number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")


    