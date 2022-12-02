from aocd import get_data,submit
import os

aoc_day=2
aoc_year=2022
part_a="a"
part_b="b"

raw_data=get_data(day=aoc_day, year=aoc_year)
strategy=raw_data.splitlines()
total_score_a=0
total_score_b=0

score_part_a={
    'A X':4,
    'A Y':8,
    'A Z':3,
    'B X':1,
    'B Y':5,
    'B Z':9,
    'C X':7,
    'C Y':2,
    'C Z':6,
}
for sign in strategy:
    total_score_a=total_score_a+score_part_a[sign]

my_answer_a=total_score_a
submit(my_answer_a, part='a',day=aoc_day,year=aoc_year)

score_part_b={
    'A X':3,
    'A Y':4,
    'A Z':8,
    'B X':1,
    'B Y':5,
    'B Z':9,
    'C X':2,
    'C Y':6,
    'C Z':7,
}
for sign in strategy:
    total_score_b=total_score_b+score_part_b[sign]

my_answer_b=total_score_b
submit(my_answer_b, part='b',day=aoc_day,year=aoc_year)