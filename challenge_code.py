## Week 16 challenge - Data in Motion
# Create a function that takes a single string as argument and returns an ordered list containing the indices of all capital letters in the string.
# e.g: index_of_caps("eDaBiT") ➞ [1, 3, 5] 

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

# output: [0, 2, 3] 

## A slight variation of the 'Crazy Kangaroo' Challenge on Hackerearth (https://www.hackerearth.com/problem/algorithm/crazy-kangaroo):
# Goal: For each test case print the number of jumps the kangaroo had to make in the range [A, B] inclusive. 
# Note: The kangaroo jumps only to those positions which are multiples of M or hop count.

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

## Week 17 challenge - Data in Motion
# 1. Given a list ["Elie", "Tim", "Matt"], create a variable called answer, which is a new list containing the first letter of each name in the list. 

names_list = ["Ellie", "Tim", "Matt"]
answer = []

for name in names_list:
    list_name = list(name)
    first_letter = list_name[0]
    answer.append(first_letter)
print(answer)

# 2. Given a list [1,2,3,4,5,6], create a new variable called answer2, which is a new list of all the even values. 

list = [1, 2, 3, 4, 5, 6]
answer2 = [num for num in list if num%2 == 0]

# output: [2, 4, 6] 

# extension: Given a list [2,4,7,3,14,19], check if a number in the list is odd (output: 'True'). Otherwise (even number): 'False'. 

l = [2,4,7,3,14,19]
for i in l:
    number = i
    odd_check = lambda i: True if number%2 != 0 else False
    print(odd_check(i))  
  
# output: False, False, True, True, False, True    
    
## Week 19 challenge - Data in Motion
# Given a list of client emails, create a function that takes in the list as an argument and returns a new list with only the domain of each email. 
# e.g: clients = ['brucewayne@gotham.com', 'homer_simpson@springfieldnuclear.com', 'hank_hill@arlenpropane.com', 'petergriffin@pawtucketbrewery.com']
# output: get_domains(clients) = ['gotham.com', 'springfieldnuclear.com', 'arlenpropane.com', 'pawtucketbrewery.com']

clients = ['brucewayne@gotham.com', 'homer_simpson@springfieldnuclear.com', 'hank_hill@arlenpropane.com', 'petergriffin@pawtucketbrewery.com']
def get_domains(clients):
    domains = []
    for email in clients:
        part_two = email.split("@")
        part_two = part_two[1]
        domains.append(part_two)
    return domains

print(get_domains(clients))

## Week 23 challenge - Data in Motion
# Define a function contains_blue() that accepts any number of arguments. It should return True if any of the arguments are "blue" (all lowercase). 
# Otherwise, it should return False. 
# contains_blue("green", False, 37, "purple", "hello world") -> output: False

def contains_blue(*input):
    true_false_list = [input[i]=="blue" for i in range(len(input))]
    return "True" if True in true_false_list else "False"
    
print(contains_blue("green", False, 37, "purple", "hello world"))

# OR alternative solution (after def contains_blue(*input)):
true_false_list = [i=="blue" for i in input]

## Week 24 challenge - Data in Motion
# Given a person variable: person = [["name", "Bruce"], ["job", "Batman"], ["city", "Gotham"]], 
# Create a dictionary called answer , that makes each first item in each list a key and the second item a corresponding value. 
# This is the end goal: {'name': 'Bruce', 'job': 'Batman', 'city': 'Gotham'}.

person = [["name", "Bruce"], ["job", "Batman"], ["city", "Gotham"]]
answer = {}
for list in person:
    answer[list[0]] = list[-1] #or list[1]

print(answer)

## Week 26 challenge - Data in Motion
# Optional bonus: Program that simulates rock, paper, scissors: 
# (Elementary game where first to 3 points wins)
import random

# Points dictionary (R beats S and P, S beats P and P beats none - slight variation):
points = {"Rock": 2, "Scissors": 1,"Paper": 0}

# Computer choice 
comp_choice_list = ["Rock", "Scissors", "Paper"]
new_comp_list_random = [comp_choice_list[random.randint(0,2)] for choice in comp_choice_list]
new_comp_list_points = [points[newchoice] for newchoice in new_comp_list_random]

# User choice
n = 0
user_choice_list = []
for n in range(3):
    user_choice = str(input("'Rock', 'Paper' or 'Scissors'? "))
    print("I chose {}!".format(new_comp_list_random[n]))
    user_choice_list.append(user_choice)
    n += 1

user_list_points = [points[userchoice] for userchoice in user_choice_list]

# Computer (c_list) and user points (u_list): 
u_list = []
c_list = []
    
for user, comp in zip(user_list_points, new_comp_list_points):  
    if user < comp:
        c_points = 1
        c_list.append(c_points)
        
    elif user > comp:
        u_points = 1
        u_list.append(u_points)

# Comparing points: 
if sum(u_list) > sum(c_list):
    print("Great, you win! You got {} points while I got {}.".format((sum(u_list)),(sum(c_list))))
elif sum(u_list) == sum(c_list):
    print("Sorry, it's a tie. You got {} points while I got {}.".format((sum(u_list)),(sum(c_list))))
else:
    print("Sorry, I win. You got {} points while I got {}.".format((sum(u_list)),(sum(c_list))))
 
## Week 35 challenge - Data in Motion
# Hard challenge: Create a function that returns the majority vote in a list. 
# A majority vote is an element that occurs > N/2 times in a list (where N is the length of the list). 
# E.g: majority_vote(["A", "A", "A", "B", "C", "A"]) ➞ "A". majority_vote(["A", "B", "B", "A", "C", "C"]) ➞ None

def majority_vote(list_of_votes):
    
    # distinct set of votes in list
    list_of_votes_copy = []
    [list_of_votes_copy.append(vote) for vote in list_of_votes if vote not in list_of_votes_copy] 
        
    # check if distinct votes in copy matches original list of votes and counting number of votes for each distinct vote
    count_list = []
    
    for vote in list_of_votes_copy:
        n = 0
        for i in range(len(list_of_votes)): 
            if vote == list_of_votes[i]:
                n += 1
        tuple_values = (n, vote)
        count_list.append(tuple_values) 
        
    for number_of_votes, distinct_vote in count_list:
        if number_of_votes > len(list_of_votes)/2:
            message = f"{distinct_vote}"
            break
        # no majority vote 
        else:
            message = "None"
    return message

majority_votes = majority_vote(["A", "B", "B", "A", "C", "C"])
print(majority_votes)  
 
## FCC interview problem: Given 2 integers L and R, count how many prime integers are on the interval [L,R].
# Note: the below code does not consider exceptions and error handling where L or R are negative, 0, the same or interchanged (L>R). 

def prime_numbers(L, R):
    total_count_list = []
    for num in range(L, R+1):
        count = [num%i == 0 for i in range(2,num)]
        total_count_list.append(sum(count))      
    n = 0 
    for i in total_count_list:
        if i == 0:
            n+=1
    return n
    
number_of_prime_numbers = prime_numbers(5, 15) # or any other numbers in interval chosen by user

## Data in Motion Challenge
# Let's assume you have a list of tuples stored in the variable transactions, each representing a transaction in an e-commerce store where the first element is the transaction ID, the second element is the product ID, and the third element is the price.
# Write a Python function to find the product with the highest total sales.

transactions = [ 
(1, 101, 15.0), 
(2, 102, 20.0), 
(3, 101, 15.0), 
(4, 103, 10.0), 
(5, 102, 20.0), 
(6, 101, 15.0), 
(7, 103, 10.0), 
(8, 102, 20.0), 
(9, 103, 10.0), 
] 

product_ids = [transaction[1] for transaction in transactions]
unique_product_ids = set(product_ids)

values = []
for id_no in unique_product_ids:
    n = 0 
    for transaction in transactions:
        if id_no == transaction[1]:
            n+=1
    tuple_values = (n, id_no)
    values.append(tuple_values)

values.sort(reverse=True)
print(values)
print(f"Product {values[0][1]} has the highest total sales. ")

for i in range(1,len(values)):
    if values[i][0] == values[0][0]:
        print(f"Product {values[i][1]} also has the highest total sales.")

