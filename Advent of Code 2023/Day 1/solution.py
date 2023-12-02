# Part 1
all_results = []
with open('advent_c_challenge1.csv', 'r') as file:
  reader = csv.reader(file)
  for row in reader:
    string = str(row)
    saved_letters = [letter for letter in string if letter.isnumeric()]
    final_saved_nos = [saved_letters[0], saved_letters[-1]]
    result = int("".join(final_saved_nos))
    all_results.append(result)
final_sum = sum(all_results)

# Part 2
a_dict = {"one": "1", "two": "2", "three": "3",
          "four": "4", "five": "5", "six": "6",
          "seven": "7", "eight": "8", "nine": "9",}

final_joined_nos = []
with open('advent_c_challenge1.csv', 'r') as file:
     reader = csv.reader(file)
     for row in reader:
         string = str(row)
         the_list = []
         initial = ""
         for letter in string:
             if letter.isnumeric():
                 the_list.append(letter)
             else:
                 initial = initial + letter 
                 for numbers in a_dict.items():
                     if numbers[0] in initial:
                         the_list.append(numbers[1])
                         initial = initial[-2:]         
         final_list = [the_list[0], the_list[-1]]
         joined_nos = int("".join(final_list))  
         final_joined_nos.append(joined_nos)
       
final_joined_nos_sum = sum(final_joined_nos)
