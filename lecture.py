
print(3+2*4/3)
print(round(3+2*4/3,4)) #round function is use to round of the number of digit 

name =input("Enter your name =")
print(name)
age = int(input("Enter your age ="))
print(age)
print(f"what is your {name} And your age {age}\n")
print("what is your {} And your age {}".format(name,age))

# this program calculate the average of 3 elements

num1=int(input("Enter the first number= "))
num2=int(input("Enter the second number= "))
num3=int(input("Enter the third number= "))
avg=(num1+num2+num3)/3
print(f"Average of number is ={str(avg)}")

 #condition in python syntax of if else and elseif condition

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a < 0:
  print("a and b are equal")
else:
  print("a is greater than b")

# This is list in python programming language

# list is the collection of ordered and changeable type of sequence

list=["hello","world","Dear","friend"]   #Deaclaration of list in python

print(list[1]) 
list.append("friend") #append function add parameter in list item after the last element

x=list.count("friend") #count function count the value of parameter in whole list
print(list)
print(x)
car= ["Volva","Corolla","Suzuki"]
list.extend(car)  # extend function merge two list into one list 
list.pop(5)  # pop function remove the value at certain place according to index 
print(list)

# touple is the collection of ordered and unchangeable sequence

touple= ("hello","world","friend") # declaration of touple 
x1=len(touple)
print(x1)

# set is the collection od unordered and unindexed sequence
 
 