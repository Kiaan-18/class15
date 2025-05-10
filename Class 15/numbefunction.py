def add(x,y):
   return x+y
def sub(x,y):
   return x-y
def mul(x,y):
   return x*y
def div(x,y):
   return x/y
num1=int(input("Enter a number:"))
num2=int(input("Enter a second number:"))
opt=input("Select operation 1. Addition\n 2. Subtraction\n 3. Multiplication \n 4. Division")
if opt=="1":
   print(add(num1,num2))
elif opt=="2":
   print(sub(num1,num2))
elif opt=="3":
   print(mul(num1,num2))
else:
   print(div(num1,num2))
   