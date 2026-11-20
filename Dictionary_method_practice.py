#------------------- Dictionary Methods ----------------------#

#A dictionary is a collection of key-values in Python.

student = [{'name': 'suruchi', 'id': 101,  'course': 'dsda', 'city': 'ayodhya'}]
print(student)
print(student[0]['name'])
print(student[0]['id'])

students_info = [{'name': 'suruchi', 'id' :101 , 'course': 'dsda'}, {'name': 'sneha', 'id': 102, 'course': 'python'} ,{'name': 'pallavi', 'id': 103, 'course': 'java'}]
print(students_info[2].values())


#1- get() method:-  specified key ki value return krta hai. (note: agar key nahi hai to key error aaega).
student = {'name': 'suruchi', 'age':22, 'course' : 'dsda'}
print(student.get('name'))
print(student.get('id'))

#2- update() method:-  dictionary me new key value pair add ya existing value update krta hai.
students = {'name':'suruchi', 'age':22, 'course':'dsda'}
students.update({'name':'sneha'})
print(students)

#3- pop() method:= 
