
# Create empty lists to process each row
list_1 = []
list_2 = []
list_3 = []

with open('input.txt', 'r') as file:
    for line in file:
        # print(line.strip())
        numbers = line.split()
        list_1.append(int(numbers[0]))
        list_2.append(int(numbers[1]))
        

for i in range(len(list_1)):
        list_3.append(abs(list_1[i] - list_2[i]))
    
# Get the sum of all values in list 3
sum_of_all_numbers = sum(list_3)

# print("Values in list 3: " + str(list_3))
print("Total: " + str(sum_of_all_numbers))
