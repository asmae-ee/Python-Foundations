#fonctions
def addition(A, B):
        return A+B
def subtraction(A, B):
        return A-B
def multiplication(A, B):
       return A*B
def division(A,B):
      return A/B

#numbers
A = float(input("enter first number: "))
B =float(input("enter second number: "))
print("chose the operation: ")
print("1_Addition")
print("2_Subtraction")
print("3_Multiplication")
print("4_Division")
choise =input("enter the number of operation: ")
if choise == "1" :
    result = addition(A, B)
elif choise == "2" :
    result = subtraction(A, B)
elif choise == "3":
   result = multiplication(A, B)
elif choise == "4":
  result = division(A, B)
else:
   result = "invalid choise"
print(result)