
# Solved with the help of ChatGPT 
# ChatGPT generated code to split pairs into start and end as well as the counter increment
# ChatGPT failed to generate correct logic for checking if pairs overlap:
# if (start1 <= start2 <= end1 <= end2) or (start2 <= start1 <= end2 <= end1):

from aocd import get_data,submit

aoc_day=4
aoc_year=2022
part_a="a"
part_b="b"

raw_data=get_data(day=aoc_day, year=aoc_year)
assignment=raw_data.splitlines()

def count_fully_contained_pairs(assignment_pairs):
    # Initialize a counter for the number of fully contained pairs
    counter_1 = 0
    counter_2 = 0
    
    # Iterate over each assignment pair
    for pair in assignment_pairs:
        # Split the pair into two assignments
        assignment1, assignment2 = pair.split(",")
        
        # Split each assignment into a start and end number
        start1, end1 = assignment1.split("-")
        start2, end2 = assignment2.split("-")
        
        # Convert the start and end numbers to integers
        start1 = int(start1)
        end1 = int(end1)
        start2 = int(start2)
        end2 = int(end2)
        
        # Check if one range fully contains the other
        if((start1 <= start2) and (end1 >= end2)) or ((start2 <= start1) and (end2 >= end1)):
            # If so, increment the counter
            counter_1 += 1

         # Check if one range  contains the other
        if(end1 >= start2 and end2 >= start1):
            # If so, increment the counter
            counter_2 += 1
    
    # Return the counter
    return [counter_1,counter_2]
    
my_answer_a = count_fully_contained_pairs(assignment)[0]

my_answer_b = count_fully_contained_pairs(assignment)[1]

submit(my_answer_a, part=part_a,day=aoc_day,year=aoc_year)
submit(my_answer_b, part=part_b,day=aoc_day,year=aoc_year)


