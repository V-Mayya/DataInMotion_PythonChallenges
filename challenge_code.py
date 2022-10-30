##Week 16 challenge - Data in Motion
#Create a function that takes a single string as argument and returns an ordered list containing the indices of all capital letters in the string.
#e.g: index_of_caps("eDaBiT") ➞ [1, 3, 5] 

def input(string):
    string_list = []
    position_of_capital_list = []
    for i in enumerate(string):
        string_list.append(i)

    for index in range(len(string)):
        the_letter = string_list[index][1]
        if the_letter.isupper() == True:
            position_of_capital = string_list[index][0]
            position_of_capital_list.append(position_of_capital)
    print(position_of_capital_list)

input("HeLLo!")

#output: [0, 2, 3] 

##A slight variation of the 'Crazy Kangaroo' Challenge on Hackerearth (https://www.hackerearth.com/problem/algorithm/crazy-kangaroo):
#Goal: For each test case print the number of jumps the kangaroo had to make in the range [A, B] inclusive. 
#Note: The kangaroo jumps only to those positions which are multiples of M or hop count.

list = [5, 10, 3] #input (A and B are integers (start and end points are inclusive), M = hop count)

A = list[0]
B = list[1]
M = list[2]

all_numbers = [A]
for i in range(B-A): 
    i = A
    A = A+1
    all_numbers.append(A)

multiples = []
for n in range(1,B+1):
    values = M*n
    multiples.append(values)

multiple_values = set(all_numbers).intersection(multiples) 
count_of_multiple_values = len(multiple_values)

print(count_of_multiple_values) #output in this case is 2






