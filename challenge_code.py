#Week 16 challenge - Data in Motion
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



