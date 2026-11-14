#1- len() function:-   The len function return the total number of characters in a string or element in a list. 'NOTE- also count space'
name = "Suruchi Upadhyay"
print(len(name))
name = "  priya Malhotra  "
print(len(name))

#2- lower() method:-   The lower method convert all character into lowercase latters.
name = "SURUCHI UPADHYAY"
CITY = "AYODHYA"
print(name.lower())
print(name.lower(),CITY.lower())

#3- upper() method:-  The upper method convert all character into uppercase latters.
name = "riya tiwari"
city = "punjab"
print(name.upper())
print(name.upper(),city.upper())

#4- title() method:-   The title method convert the first character of each word into uppercase.
name = "suruchi upadhyay"
print(name.title())
book_name = "Life is like butterfly"
print(book_name.title())

#5- capitalized() method:-   The capirtalize method convert only the first character of the string into uppercase and the remaining characters into lowercase.
name = "SURUCHI UPADHYA"
city = "ayodhya"
print(name.capitalize())
print(name.capitalize(),city.capitalize())

#6- strip() method:-    Trhe strip method remove extra space from the begining and end of a string.
name = "   Suruchi upadhyay   "
print(name.strip())

#7- replace() method:-   The replace method replace one value with another value in a string.
name = "Hello Suruchi"
print(name.replace("Suruchi","Python ji"))

#8- find() method:-    the find method return the index position of a specified character or substring.
name = "Suruchi Upadhyay"
print(name.find('U'))
print(name.find('a'))
print(name.find('z'))

#9- count() method:-   The count method return how many times a specified character or substring occurs.
name = "RADHE KRISHNA"
print(name.count('A'))
print(name.count('E'))

#10- startswith() method:-  ye chek krta hai ki string kisi particular word ya characters pr end hoti hai ya nhi, agr sahi hua to True otherwise False returne krta hai .

name = "suruchi upadhyay"
print(name.startswith('su'))
print(name.startswith('ru'))

#11- endswith() method:-   ye chek krta hai ki string kisi particular word ya characters pr end hoti hai ya nhi, agr sahi hua to True otherwise False returne krta hai .
name = "suruchi upadhyay"
print(name.endswith('yay'))
print(name.endswith('chi'))
