
# ==========================================
# Python Loops Practice
# Author: Suruchi Upadhyay
# Topics: For Loop and While Loop
# ==========================================


# 1. Print Even Numbers from 2 to 10

for i in range(2, 11, 2):
    print(i)


# 2. Print Hello 10 Times

for i in range(0, 10):
    print("Hello")


# 3. Print Numbers from 0 to 10 Using While Loop

i = 0

while i <= 10:
    print(i)
    i += 2

print("This statement is outside the loop")


# 4. Print Numbers from 20 to 50 and Increment Count

count = 15

for i in range(20, 51):
    print(i)
    count += 1
    print(count)


# 5. Check Even and Odd Numbers from 1 to 19

for i in range(1, 20):
    if i % 2 == 0:
        print("Even Number:", i)
    else:
        print("Odd Number:", i)


# 6. Multiplication Table of 2

for i in range(1, 11):
    print(2, "*", i, "=", 2 * i)

# 7. multiplication table 0f 9

for i in range(1,11):
  print(9,"*", i, "=", 9*i) 
