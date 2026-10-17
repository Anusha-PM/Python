# 1st question
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Hello, {name}! You are {age} years old.")

#2nd question
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
sum = a+b
difference = a-b
product =a*b
quotient = a%b
print(sum,difference,product,quotient)

 # 3rd Question
a = int(input("Enter your number1 in int :"))
b = int(input("Enter your number2 in int :"))
c = float(input("Enter your number3 in float:"))
avg = ((a+b+c)/3)
print(avg)

# 4th question
a = input("Enter your number:")
b = int(a)
c = float(a)
d = str(a)
print(a,type(a),b,type(b),c,type(c),d,type(d))

# 5th question 
x = 10 + 3 * 2 ** 2
print(x)

 # 6th question 
a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
a,b = b,a
print(a,b)

# 7th question
celsius_temp = input("Enter the temperature in °C:")
float_celsiustemp = float(celsius_temp)
fahrenheitTemp = (float_celsiustemp*(9/5))+32
print(fahrenheitTemp)

 # 8th question
radius = float(input("Please enter the radius:"))
pi = 3.14
area = pi*radius**2
print(area)

# 9th question 
P = float(input("Enter P : "))
R = float(input("Enter R : "))
T = float(input("Enter T : "))
SI = (P*R*T)/100
print(SI)


# 10 th question 
decimal_number = float(input("Please enter a number:"))
integral_part = int(decimal_number)
fractional_part = decimal_number - integral_part
print(integral_part)
print(fractional_part)