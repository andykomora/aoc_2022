from aocd import get_data,submit

aoc_day=3
aoc_year=2022
part_a="a"
part_b="b"

raw_data=get_data(day=aoc_day, year=aoc_year)
rucksacks=raw_data.splitlines()


common_items=[]
groups=[]
common_badge=[]

# Convert list of items to list of priorities
def priority(list_of_items):
    priority_list=[]
    for item in list_of_items:
        if item.islower():
            priority_list.append(
                ord(item) - 96
            )
        else:
            priority_list.append(
                ord(item) - 38
            )
    return priority_list

# Find Common items in 2 compartments
for rucksack in rucksacks:
    first_comp= rucksack[:len(rucksack)//2]
    second_comp = rucksack[len(rucksack)//2:]
    
    common_items.extend(list(set(first_comp).intersection(second_comp)))
    
my_answer_a=sum(priority(common_items))
submit(my_answer_a, part=part_a,day=aoc_day,year=aoc_year)


# Find common badges in groups of 3 rucksacks
for i in range (0,len(rucksacks),3):
    groups.append(rucksacks[i:i+3])

for group in groups:
    common_badge.extend(list(set(group[0]).intersection(group[1]).intersection(group[2])))

my_answer_b=sum(priority(common_badge))
submit(my_answer_b, part=part_b,day=aoc_day,year=aoc_year)