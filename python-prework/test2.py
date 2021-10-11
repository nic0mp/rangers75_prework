 # def hello_name(user_name):
#     print("hello " + user_name + "!")

# hello_name("Chunks")

#Question 2 
# Print first 100 odd numbers  between 1 and 100 in Python.
# odd_numbers = list(range(1,100,2))
# print(odd_numbers) MY ANSWER

#print all odd numbers bet 1 and 100
# def add100():
#     print([value for value in range(1, 100, 2)])

# add100()

#Print first 100 odd numbers
# def first_100():
#     numbers = list(range(0,201))
#     for number in numbers:
#         if number % 2 != 0:
#             print(number)

# first_100()

#Question 3 
# Please write a Python function, max_num_in_list to return the max number of a given list. 
# def max_num_in_list(a_list):
#     print(max(a_list))
# max_num_in_list([1, 2, -5, -7, 9, -12])

# def max_num(a_list):
#     max_value = max(a_list)
#     return max_value

# print(max_num([2,3,5,8,7]))
# test = max_num([2,3,5,8,7])

#Question 4 
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, 
# but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).
# def is_leap_year(year):
#      if (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
#         print("True")
#      else:
#         print("False")
# is_leap_year(2004)

# def is_leap_year(a_year):
#     if a_year % 4 == 0 and (a_year % 400 == 0 or a_year % 100 != 0):
#         print(True)
#     else:
#         print(False)

# is_leap_year(2022)

#Question 5 
# Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.

# def is_consecutive(a_list):
#     return sorted(a_list) == list(range(min(a_list),max(a_list)+1))

# print(is_consecutive([1,2,3,5,6,]))

def is_consecutive(a_list):
    i =0
    status = True
    while i < len(a_list) - 1:
        if a_list[i] + 1 == a_list[i+1]:
            i+=1
        else:
            status = False
            break
    print(status)

is_consecutive([1,2,3,5,6,])
is_consecutive([1,5,3,2])

    