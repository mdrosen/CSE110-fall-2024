'''Instructions
Ask the user for a series of numbers, and append each one to a list. Stop when they enter 0.
Once you have a list, have your program do the following:

Core Requirements
Work through these core requirements step-by-step to complete the program. Please don't skip ahead and do the whole thing at once, because others on your team may benefit from building the program up slowly.
Compute the sum, or total, of the numbers in the list.
Compute the average of the numbers in the list.
Find the maximum, or largest, number in the list.
The following shows the expected output:

Enter a list of numbers, type 0 when finished.
Enter number: 18
Enter number: 36
Enter number: 2
Enter number: 48
Enter number: 6
Enter number: 12
Enter number: 9
Enter number: 0
The sum is: 131
The average is: 18.714285714285715
The largest number is: 48
Stretch Challenge
Have the user enter both positive and negative numbers, then find the smallest positive number (the positive number that is closest to zero).
Sort the numbers in the list and display the new, sorted list. Hint: There are python libraries that can help you here, try searching the internet for them.'''



numbers = []
while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        break
    else:
        numbers.append(number)
        
num_sum=sum(numbers)
avg_num=num_sum/len(numbers)
num_max=max(numbers)

pos_numbers=[num for num in numbers if num > 0]
pos_num_min=min(pos_numbers)

num_sort=sorted(numbers)
pos__num(numbers):
    positive_numbers = [num for num in numbers if num > 0]
    if positive_numbers:
        return min(positive_numbers)
    else:
        return None

print(f'the sum of numbers is: {num_sum}')
print(f'The average of the numbers is: {avg_num}')
print(f'The largest number is: {num_max}')
if pos_num_min is not None:
        print(f'The smallest positive number is:{pos_num_min}')

print(f'the sorted list of numbers is: {num_sort}')