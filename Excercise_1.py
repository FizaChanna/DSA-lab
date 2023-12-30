# Exercise 1: Basic List Operations
# 1.Create a list of integers and perform the following operations:
# a.Print the list.
list_1 = [1,2,3,4,5]
print("print list: ",list_1)
# b.Find the length of the list.
length = len(list_1)
print("Length of list: ",length)
# c.Access and print the first and last elements of the list.
first_element = list_1[0]
last_element = list_1[(length-1)]
print("Access First element from list: ",first_element)
print("Access last element from list: ",last_element)
# 2.Concatenate two lists and print the result.
list_2 = [3,6,2,9,1]
conncat = list_1 + list_2
list_1.extend(list_2)
print("concatenate the two lists",list_1)
print("concatenate the two lists",conncat)
# 3.Remove duplicates from a list.
set_list = set(conncat)
print(set_list)
Unique_list = list(set_list)
print("Romovable duplicate list: ",Unique_list)