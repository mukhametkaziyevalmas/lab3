
user_input = input("Enter a string without whitespaces: ")


char_tuple = ()

for char in user_input:
    char_tuple += (char,)


print("Created tuple is:")
print(char_tuple)




# 2
char_tuple = ('T', 'h', 'e', 'B', 'i', 'g', 'B', 'e', 'n')


resulting_string = ''.join(char_tuple)

print("The string is:", resulting_string)


#3

tuple_A = (1, 2, 3, 4, 5, 6, 7)
tuple_B = (5, 6, 7, 9, 7, 1, 10, 10)


len_A = len(tuple_A)
len_B = len(tuple_B)

mid_A = len_A // 2
mid_B = len_B // 2

result_tuple = tuple_A[:mid_A] + tuple_B[mid_B:]

print(result_tuple)

# 3
input_tuple_1 = (55, 6, 777, 54, 6, 76, 7777, 1, 777, 6)


def count_occurrences(input_tuple):
    element_count = {}
    for element in input_tuple:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    
    output_tuple = tuple((key, value) for key, value in element_count.items())
    return output_tuple


output_tuple_1 = count_occurrences(input_tuple_1)



print("Elements and their occurrences (Sample 1):")
print(output_tuple_1)

#4

sample_input_1 = (55, 6, 777, 70.0, '7', 'A')


result_tuples = []
current_tuple = ()
current_type = None

for item in sample_input_1:
    item_type = type(item)
  
    if item_type != current_type:
        if current_tuple:
            result_tuples.append(current_tuple)
        current_type = item_type
        current_tuple = ()
    
    current_tuple += (item,)

if current_tuple:
    result_tuples.append(current_tuple)

for tup in result_tuples:
    print(tup)

    #5

user_input = input("Enter a string without whitespaces: ")

char_set = {char for char in user_input}


print("Created set is:")
print(char_set)


#6

set_A = {1, 2, 3, 4, 5}
set_B = {5, 7, 8, 9, 2, 10}

difference_set = set_A - set_B

print(difference_set)

#7

set_A = {1, 2, 3, 4, 5}
set_B = {5, 7, 8, 9, 2, 10}

set_A.difference_update(set_B)

print(set_A)

#8

set_A = {1, 2, 3, 4, 7}
set_B = {8, 7, 9, 4, 2, 0, 10}
set_C = {4, 0, 1}


for element in set_A.copy():  
    if element in set_C:
        set_A.remove(element)
        set_B.add(element)

set_C.update(set_A)

print("Updated set_C =", set_C)

#9
from itertools import combinations

A = {1, 2, 3, 4, 5, 6}
n = 3
m = 5

combinations_list = []

for combo in combinations(A, n):
    combinations_list.append(set(combo))


if len(combinations_list) < m:
    print("Cannot generate", m, "unique sets of size", n, "from the superset A.")
else:
 
    print(combinations_list[:m])

#10
from itertools import groupby


cars_list = [('BMW', 'X6'), ('Toyota', 'Yaris'),
             ('Fiat', '500'), ('Fiat', 'Panda'), ('Toyota', 'Camry 30')]

sorted_cars_list = sorted(cars_list, key=lambda x: x[0])


grouped_cars = groupby(sorted_cars_list, key=lambda x: x[0])


for manufacturer, group in grouped_cars:
    group_count = len(list(group))
    print(manufacturer, group_count)
    for model in sorted([model for _, model in group]):
        print('-', model)

