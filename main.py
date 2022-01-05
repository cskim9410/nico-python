x = [1, 2, "3"]

print(x[1])

def say_hello(name="annonymous") :
  print(f"Hello {name}")

say_hello()
say_hello("KCS")

def plus(a, b):
  return int(a) + int(b)

def minus(a, b):
  return a - b

def division(a, b):
  return a/b

def times(a,b):
  return a*b

def power(a,b):
  return a**b

def negation(a,b):
  return a%b


result = plus(5, "5")

print(result)

def age_check(age):
  if age < 18:
    print("too young")
  elif age >18 and age<25:
    print("you are still kind of young")
  else:
    print("enjoy!")

age_check(53)
  
days = ("Mon", "Tue", "Wed", "Thu", "Fri")

for day in days:
  if day is "Wed":
    break
  else:
    print(day)

t1=[]
t2=[]
t3=t1

result1 = (t1 is t2)
result2 = (t2 is t3)
result3 = (t3 is t1)

print(result1)
print(result2)
print(result3)

from math import fsum, ceil

print(ceil(1.2))

import