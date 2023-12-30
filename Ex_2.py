import random 
# Exercise 2: List Manipulation
random_list =[]
for i in range(10):
    random_list.append(i)
random.shuffle(random_list)
# 1.Write a Python program to find the second-largest number in a list.
set_list = set(random_list)
unique_list = list(set_list)
sec_lar_num = unique_list[-2]
print("List: ",unique_list)
print("Seocnd largest number is: ",sec_lar_num) 

# 2.Implement a function to reverse a list.
unique_list.reverse()
print("Reverse list: ",unique_list)

# 3.Write a program to shuffle a list randomly.
print("Shuffled list: ",random_list)