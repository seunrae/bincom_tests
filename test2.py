import random
def recursive_search(arr, target, index=0):
	if index == len(arr):
		return -1;
	elif arr[index] == target:
		return index;
	else:
		return recursive_search(arr, target, index + 1);

numbers_list = [2, 4, 6, 8, 10, 12, 14, 16];
user_input = int(input("Enter a number to search in the list: "))
result = recursive_search(numbers_list, user_input)

if result != -1:
    print(f"The number {user_input} is found at index {result}.")
else:
    print(f"The number {user_input} is not in the list.")

# 8. Generate Random 4-Digit Binary Number and Convert to Base 10:
binary_number = ''.join(random.choice('01') for _ in range(4));

decimal_number = int(binary_number, 2);
print(f"generated Binary number: {binary_number}");
print(f"Converted to Base 10: {decimal_number}");

# 9. Sum the First 50 Fibonacci Numbers:
def fibonacci_sequence(n):
	sequence = [0 , 1];
	while len(sequence) < n:
		sequence.append(sequence[-1] + sequence[-2])
	return sequence;

fibonacci_numbers = fibonacci_sequence(50);
sum_of_fibonacci = sum(fibonacci_numbers);

print(f"The sum of the first 50 Fibonacci numbers is: {sum_of_fibonacci}")
	
	
