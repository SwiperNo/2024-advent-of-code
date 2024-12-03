# ref https://www.geeksforgeeks.org/python-count-occurrences-element-list/
from collections import Counter

# Create empty lists to process each row
# List on the right
list_1 = []
# List on the left
list_2 = []

with open('input.txt', 'r') as file:
    for line in file:
        # print(line.strip())
        numbers = line.split()
        list_1.append(int(numbers[0]))
        list_2.append(int(numbers[1]))

# list_1.sort()
# list_2.sort()

# Find occurances  of each number in
occurances_counter = Counter(list_2)

print(f"Checking values {occurances_counter}")

sim_score = 0
for i in list_1:
    sim_score += i * occurances_counter[i]
        
print(f"Total: {sim_score}")
