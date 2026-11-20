#---------------- if-else ---------------------
'''
#Q1. Check Even or Odd Number
#Write a program to check whether a number is even or odd

num = int(input("Enter a number:"))

if num % 2 == 0:
  print("Even number")
else:
  print("Odd number")
'''
'''

#Q2. Check Positive, Negative or Zero

num = int(input("Enter a number:"))

if num > 0:
  print("Positive")
elif num < 0:
  print("Negative")
else:
  print("Zeero")
'''
'''
#Q3. Find the Greatest Number Between Two Numbers

a = 40
b = 30

if a > b:
 print("A is greater")
else:
 print("B is greater")
'''
'''
#Q4. Check Voting Eligibility

num = int(input("Enter the number:"))

if num >= 18:
  print("eligible for vote")
else:
  print("not eligible")
'''
'''
#Q5. Check Password
 
user = "suruchi"
password = "python123"

 
user_password = input("Enter the password:")
user_name = input("Enter the name:")

if user == user_name and password == user_password:
  print("login successdul")
else:
  print("wrong password")
'''
'''
#Q6. Student Pass or Fail
#passing marks  are = 40

marks = int(input("Enter the Number:"))
if marks >= 40:
   print("pass")
else:
   print("fail")
'''
'''
#Q7. Check Divisibility by 5

num = int(input("Enter the number"))

if num %5 == 0 :
  print("divisible by 5")
else:
  print("this is not divisible")
'''
'''
#Q8. 8.	Write a program to calculate a student's grade based on marks: A for 90+, B for 75–89, Cfor 60–74, D for 40–59, otherwise Fail.

mark = int(input("Enter the mark:"))

if mark >= 90:
  print("Grade A")
elif mark >75:
  print("Grade B")
elif mark >60:
  print("Grade C")
elif mark >40:
  print("Grade D")
else:
  print("Fail")
'''
'''
#Q9.Write a program to find the greatest among three numbers.

a = 10
b = 25
c = 15

if a > b and a > c:
    print("A is greatest")
elif b > a and b > c:
    print("B is greatest")
else:
    print("C is greatest")
'''
'''
a = 30
b = 50
c = 90
num1 = int(input("Enter the number:"))
num2 = int(input("Enter the number:"))
num3 = int(input("Enter the number:"))

if num1 > a:
 print("greater number hai")
elif num2 > b:
 print("greater number hai")
elif num3 > c:
 print("greater number hai")
else:
 print(small)
'''
#10.Write a program to check whether a year is a leap year.

year = int(input("Enter year:"))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
   print("Not a Leap Year")