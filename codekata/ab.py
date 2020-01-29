def rand()
from random import randint
a = int(input("enter the number:"))
b = randint(0,9)
print("the random numberis:",b)
if a == b:
  print("won")
else:
  print("lose")  
rand()
