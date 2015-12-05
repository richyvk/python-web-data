# Find all numbers in a text document and sum them

import re

allNumbers = []

with open('regex_sum_190010.txt') as f:
    text = f.read().splitlines()

for line in text:
    numbers = re.findall('[0-9]+', line)
    for number in numbers:
        allNumbers.append(int(number))

print sum(allNumbers)