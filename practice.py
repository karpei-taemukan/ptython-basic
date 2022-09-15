days = ["m","t","w"]
print(type(days))
print("m" in days)
print(len(days))
print(min(days))
print(max(days))
days.append(2)
print(days)
days.reverse()
print(days)

day = ("m", "t", "w")
print(type(day))
print("m" in day)
print(len(day))
print(min(day))
print(max(day))
days.append(2)
print(day)
days.reverse()
print(day)

nico = {
  "name" : "Nico",
  "age" : 29,
  "korean" : True,
"fav_food" : ["Kimchi", "Sashimi"]
}
print(nico)
print(nico["fav_food"])
nico["handsome"] = True;
print(nico)


age= "18"
n_age = int(age)
print(type(n_age))


def say_hello(who = "annoymous"):
  print("hello" , who, 2, "lala", False, 2.3)
  print("bye")  

say_hello(True)
say_hello()


def p_plus(a, b = 5):
  print(a + b)
p_plus(2, 4)
p_plus(4)


def r_plus(a, b = 0):
    return a + b
    print("lalala")

p_result = p_plus(2, 3)
r_result = r_plus(2, 3)

print(p_result, r_result)


def minus(a, b):
    return int(a) - int(b)

min = minus(b = 10, a = "3")

print(min)

def said_hello(name, age):
    return f"Hello {name} you are {age} years old"

hello = said_hello( name = "nico", age = "12")

print(hello)

def plus(a, b):
    if type(b) is int or type(b) is float:
        return a + b
    else:
        return None

print(plus(21, "4"))


def age_check(age):     
  print(f"You are {age}")
 
  if age < 18:
     print(f"You can't drink")

  elif age == 18 or age == 19:
      print("You are new to this")
    
  elif age >= 20 and age <= 25:
     print("You are still kind of young")
  
  else:
    print("You can drink")

age_check(19)

week = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

for weeks in week:
    print(weeks)

for x in [1,2,3,4]:
  if x == 3:
      break
  else:
      print(x)

for y in "nicolas":
    print(y)

from math import ceil, fabs as absol, fsum

print(ceil(1.2))
print(absol(-1.2))
print(fsum([1, 2, 3, 4, 5, 6, 7]))


from calculator import plus_plus, minus_minus
print(plus_plus(2,4), minus_minus(3,6))

