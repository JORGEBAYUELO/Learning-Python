# if 4 + 5 == 10:
#     print("TRUE")
# else:
#     print("FALSE")
# print("TRUE")

# x = -10
# if x < 0:
#     print("The negative number ", x, " is not valid here.")
# print("This is always printed")

# x = 3
# if (x == 0):
#     print("Am I here")
# elif (x == 3): 
#     print("Or here")
# print("Or over here")

# if True: print("hello")

# if (5,10):
# print("hello")

# if (yes):
#     print("hello")

# if (5,10): print("hello")

# x = 0 
# while (x < 50):
#     x+=2

# print(x)

# i = 1
# while True:
#     if i%3 == 0:
#         break
#     print(i)
#     i += 1

# i = 1
# while True:
#     if i % 0o7 == 0:
#         break
#     print(i)
#     i += 1

# i = 5
# while True:
#     if i % 0o11 == 0:
#         break
#     print(i)
#     i += 1

# i = 2
# while True:
#     if i%3 == 0:
#         break
#     print(i)
#     i += 2

# i = 1
# x = 3
# sum = 0
# while (i <= x):
#     sum += i
#     i += 1
# print(sum)

# x = 1
# while (x < 20):
#     x = x * 2
# print(x)

# x = 2021
# for i in x:
#     print(i)

# is_hungry = True
# if(not is_hungry):
#     print("You are not hungry")
# else:
#     print("You are hungry")

# x = 6
# y = 7
# print(x == y)

# x = 2
# x << 4

# numbers = [1, 2, 3, 4, 5]
# numbers[4] = 6
# print(numbers[4])

# list1 = [1, 2, 3, 4, 5]
# print(list1[4])

# list1 = [1, 2, 3, 4, 5]
# list1[0] = 10
# print(list1)

# list1 = [10, 11, 12, 13, 14]
# print(list1[::3])

# list1 = ["UK", "India", "Canada"]

# list1.insert(1,8)

# print(list1)

# list1 = [10, 20, 30, 40, 50]
# list1.append(60)
# print(list1)

# ages = [56, 72, 24, 46]
# ages.sort()
# print(ages)

# list1 = ["Go", "Java", "C", "Rust"]
# print(min(list1))

# list1 = ["Go", "Java", "C", "Python"]
# print(max(list1))

# num = [4, 4, 3, 1]
# num.sort()
# print(num)

# list1 = [4, 4, 3, 1]
# list1.pop(2)
# print(list1)

# sum = 0 
# values = [2,9,1,7]
# for number in values:
#     sum = sum + number
# print(sum)

# sum = 0 
# values = [2,9,1,7]
# for number in values:
#     sum += number
# print(sum)
 
# for x in [0, 1, 1, 3]:
#     for y in [0, 2, 1, 2]:
#         print('*')

# for letter in 'KodeKloud':
#     if letter == 'u':
#         continue
#     print("Letter : " + letter)

# list1 = [4,0,7,1]
# print(list1[::-1])

# letters = ["A", "B", "C", "D", "E"]
# print(letters[1:])

# list1 = [10, 11, 12, 13, 14]
# list1.append(15)
# print(list1)

# list1 = [[1,2,3,2,5],[4,5,6,7],[8,9,10]]
# for i in list1:
#     if len(i) == 3:
#         print(i)

# list1 = [[1,2,3,2,5],[4,5,6,7],[8,9,10]]
# for i in list1:
#     if len(i) == 4:
#         print(i)

# list1 = [1, 2, 3, 4]
# for i, j in enumerate(list1):
#     print(i, j)

# list1 = [1, 2, 3, 4]
# for index, j in enumerate(list1):
#     print(index, j)

# list1 = [10, 11, 12, 13, 14]
# print(list1[::1])

# my_list = [0, 1, 2, 3, 4]
# print(my_list[::-1])

# list1 = [1, 66, "python", [11,55, "cat"], [ ], 2.22, True]
# print(list1.upper())

# my_list = [0, 1, 2, 3, 4]
# my_list.append("python")
# b = my_list[1:]
# print(b)

# countries = ["USA", "Canada", "India"]
# countries[0], countries[1] = countries[1], countries[0]
# print(countries)

# matrix = [[j for j in range(4)] for i in range(4)]
# print(matrix[3][1])

# matrix = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

# matrix2 = []

# for submatrix in matrix:
#     for val in submatrix:
#         matrix2.append(val)
# print(matrix2[0])

# countries = [["Egypt", "USA", "India"], 
#              ["Dubai", "America", "Spain"],
#              ["London", "England", "France"]]
# countries2 = [country for sublist in countries for country in
#               sublist if len(country) < 4]
# print(countries2)

# a = []
# for i in range(2):
#     a.append([])
#     for j in range(2):
#         a[i].append(j)
# print(a)

# Colors= [ [['Blue','Green','White','Black']], [['Green','Blue','White','Yellow']] , [['White','Blue','Red','Green']] ]

# print(Colors[2][0][2])

# matrix = [[[k for k in range(3)] for j in range(3)] for i in range(3)]
# print(matrix[0][0][1])

# matrix = [[[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]

# matrix2 = []

# for submatrix in matrix:
#   for val in submatrix:
#     matrix2.append(val)

# print(matrix2[2][2])

# matrix = [[[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]
# print(matrix[0][0][0])

# def my_function(*students):
#   print("The tallest student is " + students[2])

# my_function("James", "Ella", "Jackson")

# def multi_func():
#   result = int(input()) * 5
#   return result     

# print(result)

# a = 0
# def add_one(a):
# 	return a+1

# result = add_one(a)
# print(result)

# def print_info(name, age=18):
#     print(name, age)

# print_info('john', 19)

# Function :  def add_func(num1,num2):
#                    	return num1 + num2
 
# Sample input: print ( add_func(5 , num1= 10) )

# Function :  def add_func(num1,num2):
#             	  	return num1 + num2 	
# print( add_func(5 , 5) )

# def my_function(*friends):
#   print("The tallest student is " + friends[0])

# my_function("john", "Ella", "mark")

# nums= [7,4,1]
# def change_third_item(list):
# 	list[2] = 5

# change_third_item(nums)
# print(nums)

# a = 0
# def add_three(a):
# 	return a+3

# result = add_three(a)
# print(result)

# a = 0
# def add_three(a):
# 	return a+3

# result = add_three(3)
# print(result)

# def print_name_age(name, age=19):
#     print(name, age)

# print_name_age('john', 18)

# def fullname_func(fname):
#   print(fname + " Mark")

# fullname_func("John")

# def fullname_func(fname, lname):
#   print(fname + " " + lname)

# fullname_func("John", "Mark")

# def my_function(x):
#   return 5 + x

# print(my_function(3))


# def my_function(x):
#   return 10 - x

# print(my_function(4))

# def my_function(x):
#   return 10 / x

# print(my_function(2))

# def square(i):
#     j = i * i
#     return j

# print(square(3))

# def square(i):
#     j = i * i
#     return j

# num = 2
# result = square(num)
# print("The result of ", num, " is ", result)

# def add(x, y):
#   return x+y

# def return_greeting():
#   return "Hello, World"

# print(return_greeting())

# def is_true(a): 
#   return bool(a) 

# result = is_true(3<6) 
# print("The result is", result)

# def is_true(a): 
#   return bool(a) 

# result = is_true(6<3) 
# print("The result is", result)

# def get_odd_func(numbers):
#     odd_numbers = [num for num in numbers if num % 2]
#     return odd_numbers

# print(get_odd_func([1, 2, 3, 4, 5, 6]))

# def mean_func(list1):
#     return sum(list1) / len(list1)

# print(mean_func([5, 2, 2, 4]))

# def mean_func(list1):
#     return sum(list1) / len(list1)

# print(mean_func([5, 6, 7, 8]))

# def my_function(names):
#   for i in names:
#     print(i, end=' ')

# names = ["john", "mark", "emmy"]
# my_function(names)

# def my_function(numbers):
#   for i in numbers:
#     print(i+1, end=' ')

# numbers = [1, 2, 3] 
# my_function(numbers)

# def my_function(numbers):
#   for i in numbers:
#     print(i*2+10, end=' ')

# numbers = [1, 2, 3]
# my_function(numbers)

# def double_list(numbers):
#   return 2 * numbers

# numbers = [1, 2, 3]
# print(double_list(numbers))

# def myfunc():
#   a = 20
#   print(a)

# myfunc()

# def my_function():
#   x = 20
#   def my_inner_function():
#     print(x)
#   my_inner_function()
# my_function()

# def my_function():
#   def my_inner_function():
#     x = 20
#     print(x)
#   my_inner_function()

# my_function()

# def my_function():
#   def my_inner_function():
#     x = 20
#   print(x)
#   my_inner_function()

# my_function()

# x = 20
# def my_function():
#   print(x, end=' ')

# my_function()
# print(x, end=' ')

# x = 20
# def my_function():
#   x = 30
#   print(x, end=' ')

# my_function()
# print(x, end=' ')

# x = 20
# def my_function():
#   x = 30
#   print(x, end=' ')

# my_function()
# print(x, end=' ')

# def my_function():
#   global x
#   x = 30

# my_function()
# print(x)

# x = 30
# def my_function():
#   global x
#   x = 20

# my_function()
# print(x)

# def my_function(*ages):
#   print("The older friend is " + ages[0] + " years")

# my_function("13", "12", "11")

# def my_function(*argv):  
#     for arg in argv:  
#         print(arg) 

# my_function('Hello', 'World!')

# def my_function(arg1, *argv): 
#     print ("First argument:", arg1) 
#     for arg in argv: 
#         print("Next argument:", arg) 

# my_function('Welcome', 'to', 'Python!')

# def sum(a,b):
#     return a+b

# print(sum(2,3))

# def division(a,b):
#     return a/b

# division(8,2)

# def my_function(*argv):
#   print(argv)

# my_function('Hello', 'World!')

# def my_function(*argv):
#   print(argv[0])

# my_function('Hello', 'World!')

# def sum(*args):
#     for arg in args:
#         result += arg
#     return result 

# print(sum(2,3,1))

# tuple1 = (1,2,3,4,5)
# print(tuple1.append(6))

# x = tuple(3)
# print(x)

# a = (10, [20, 30], 40, 50)
# a = a[1][1]
# print(a)

# testdict = {
#   "brand": "Samsung",
#   "ram": "3",
#   "Os": "Android",
#   "year": 2020
# }

# testdict.update({'brand':'oppo' })
# print(testdict)

# try:
#       print("my_string"[1/0])
# except IndexError:
#       print("index error")
# except ZeroDivisionError:
#       print("zero error")
# except:
#       print("other error")

# try:
#       x = y + 1
# except NameError:
#       print("y is not defined")

# try:
#       x = 'seasalt'[7]
# except IndexError:
#       print("No character found in that index")

# try:
#       x = 'y' + 1
# except ValueError:
#       print("y is not a number value")

# try:
#     x = y + 1
# except NameError:
#     print("y is not defined")
#     x = y + 1

# try:
#     y = 5 / 0
# except ZeroDivisionError:
#     print("Can't divide with zero.")

# try:
#     z = 3 // 0
# except ZeroDivisionError:
#     print("Zero won't work!")
# except ArithmeticError:
#     print("We have a problem!")

# a = input("Enter a number: ")
# try:
#     float(a) / 0
# except (TypeError, ZeroDivisionError):
#     print("Please enter valid numbers, besides zero.")

# matrix = [[[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]

# matrix2 = []

# for submatrix in matrix:
#   for val in submatrix:
#     matrix2.append(val)

# print(matrix2[2])

# def my_function():
#   x = 20
#   def my_inner_function():
#     print(x)
#   my_inner_function()
# my_function()

# Num = input("Enter a Number: ") 
# print (Num * 3 )

# def my_function(arg1, *argv): 
#     print ("First argument:", arg1) 
#     for arg in argv: 
#         print("Next argument:", arg) 

# my_function('Welcome', 'to', 'Python!')

def sum(*args):
    result = 0
    for arg in args:
        result += arg
    return result 

print(sum(2,3,1))