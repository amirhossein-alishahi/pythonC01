# 1  
my_set = set([1,2,3,4,5,6,7,8,9,10])

# 2 
my_list = list(my_set)

# 3
my_list.remove(9)
my_list.remove(10)
my_list.remove(3)
my_list.remove(5)
my_list.insert(0,5)
my_list.remove(4)
my_list.insert(1,4)
my_list.insert(2,6)
my_list.insert(3,7)
my_list.insert(6,4)
print(my_list)

# 4 
print(my_list[3:6])

# 5 
set_from_list = set(my_list)

# 6 
print(set_from_list)

# 7 
del set_from_list


# 8 
my_string = "این یک مثال است"
my_words_list = my_string.split()

# 9
print(my_words_list)
