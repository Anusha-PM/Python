# 1st question
salary = int(input("Please enter your salary:"))
if(salary<30000):
    tax_rate = 5
elif(salary<=70000):
    tax_rate = 15
else:
     tax_rate = 25
print("Final tax_rate",tax_rate,"%")

# 2nd question
def even_number(a,b):
    for i in range(a,b+1):
        if(i%2==0):
            print(i)

even_number(1,100)

# 3rd Question
n = 312
while(n>0):
    ld=n%10
    print(ld)
    n//=10

# 4th Question
n = 312
count=0
while(n>0):
    count+=1
    n//=10
print(count)

# 5th question
n = 312
digit_sum=0
while(n>0):
    ld=n%10
    sum+=ld
    n//=10
print(sum)

# 6th question
for i in range(1,100):
    if(i%3==0 and i%5==0):
        print(i)

# 7th Question
while(True):
    value = (input("Please enter your value:"))
    if(value=="Quit"):
        break

#     value = int(value)
    if(value>0):
        print("Positive")
    elif(value<0):
        print("Negative")
    else:
        print("Zero")
    
# 8th Question
def calculator(a,b,operation):
    if(operation == "+"):
        return a+b
    elif(operation == "-"):
        return a-b
    elif(operation == "*"):
        return a*b
    elif(operation == "/"):
        return a/b
    else:
        print("Invalid input")
print(calculator(5,6,""))


# 9th Question 
import math
def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            return False
        
    return True

print(is_prime(9))
        
# 10th Question 
n=5
while(True):
    guess_num = int(input("Please enter the number you guessed:"))
    if(guess_num==n):
        print("Correct!")
        break
    elif(guess_num>n):
        print("Too high")
    else:
        print("Too low")