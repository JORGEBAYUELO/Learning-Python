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