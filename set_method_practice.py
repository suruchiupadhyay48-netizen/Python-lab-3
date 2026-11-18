#------------set methods ----------------------

#1- add() method:- Adds a single element to the set.
fruit = {'apple', 'banana', 'mango'}
fruit.add('orange'),fruit.add('guava')
print(fruit)

#2-update() method:- Adds multiple elements to the set.
fruit = {'apple', 'banana', 'mango'}
fruit.update(['guava','papaya', 'lichi'])
print(fruit)
print(type(fruit))

#3-remove() method:-  remove the specified element from the set. If  the element is not present,it raises an error. 
fruit = {'apple', 'banana', 'mango'}
fruit.remove('apple')
print(fruit)

#4-discard() method:-   Remove the specified element from the set. If element is not present, it does not raise an error. 
name = {'suruchi', 'sneha', 'pallavi'}
name.discard('ensha')
print(name)
name.discard('suruchi')
print(name)

#5- pop() method :-   Remove and returns an arbitary element from the set. [note: A set is unorderd, so it cannot be predicted which element will be removed.
number = {50,10,20,30}
number.pop()
print(number)

#6- clear() method:-  Remove all elements from the set.
number = {10,20,30,40,50}
number.clear()
print(number)

