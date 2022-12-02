from aocd import get_data
import os

AOC_SESSION = os.getenv("AOC_SESSION")
data=get_data(day=1, year=2022)
data_into_list = data.splitlines()

callories_sum=0
list_of_sums=[]

for i in data_into_list:
    
    if i!='':
        callories_sum=callories_sum+int(i)
        
    else:
        list_of_sums.append(callories_sum)
        callories_sum=0

#Most Calories
print(max(list_of_sums))

#Sum of Top 3 calories
sorted_list_of_sums=sorted(list_of_sums,reverse=True)
list_of_top_three=sorted_list_of_sums[0:3]
sum_of_top_three=sum(list_of_top_three)

print(sum_of_top_three)