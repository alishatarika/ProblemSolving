# from functools import reduce


# print("Hello world")
# a=int(input("tell your age"))
# '''function'''
# def function():
#   '''lmflrmlrm'''
#   print("GOOD")

# function()
# print(function.__doc__)
# '''list'''
# lis =[1,9,3]
# lis.sort()
# print(list)
# lis.reverse()
# print(list)
# lis.append(45)
# print(list)
# lis.insert(2,56)
# print(list)
# lis.pop()
# print(list)
# lis.remove(3)
# print(list)
# m=[67,78,56,45]
# lis.extend(m)
# print(lis)
# '''string'''
# string="alisha"
# print(string[1:3])
# print(len(string))
# print(string.count("c"))
# print(string.find("a"))
# print(string.capitalize())
# print(string.replace("a","i"))
# print(string.endswith("sha"))
# print(string[4])
# '''tuple'''
# rest=(1,4)
# print(rest)

# def recursionfibo(n): 
#  n1=0
#  n2=1
#  for i in range(1,n):
#   print(n1,end=" ")
#   sum=n1+n2
#   n1=n2
#   n2=sum
# recursionfibo(10)
# t=(1,2,3)  
# '''tuple'''
# te=list(t) 
# '''set not take repeated value'''
# s={1,3,4,5,3}
# print(s)
# print(type(s))


# dic={
#   344:"harry",
#   56:"shubam"
  
# }
# print(dic)
# print(dic[344])
# print(dic.get(344))
# print(dic.keys())

# try:
#  num=int(input("Enter a number "))

# except:
#   print("invalid choice")
# finally:
#   print("i am always ready")
  
# f=89
# h=76
# print(h) if f<h else print("no")
# '''
# enum'''
# marks=[34,67,89,56,34]
# for index,mark in enumerate(marks):
#  print(index,marks[index])
  
# cube = lambda y: y*y*y 
# print(cube(4))
# lit =[3,5,6,7]
# print(list(map(cube,lit)))
# def filterf(a):
#   return a>5
# print(list(filter(filterf,lit)))

# def sum(x,y):
#   return x-y
# print(reduce(sum,lit))

# you=(5,8,9)
# she=(5,8,9)
# print(you is she)
# print(you == she)

# u=[6,7,8]
# y=[6,7,8]
# print(y is u)
# print(y == u)
class person:
    

   def __init__(self,n,o) :
     self.name=n
     self.roll_no=o
      
   def info(self):
        print(self.name, self.roll_no)

ay = person("alisha",56)

ay.info()
import random
n=random.randint(0,7)
print(n)
import random
 
# Randomly generate a ascii value
# from 'a' to 'z' and 'A' to 'Z'
randomLowerLetter = chr(random.randint(ord('a'), ord('z')))
randomUpperLetter = chr(random.randint(ord('A'), ord('Z')))
print(randomLowerLetter, randomUpperLetter)
stribg="alisha-12200"
print(stribg.split("-")[0])

ar="alish"
print(len(ar))




  
