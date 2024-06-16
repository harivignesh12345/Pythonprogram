Complete the program to count frequency of each element of an array. Frequency of a particular element will be printed once.

 

Sample Test Cases

 

Test Case 1

 

Input

 

7

23

45

23

56

45

23

40

 

Output

 

23 occurs 3 times

45 occurs 2 times

56 occurs 1 times

40 occurs 1 times
numbers = []
n = int(input())
for _ in range(n):
    num = int(input())
    numbers.append(num)

frequency = {}
for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

for number, count in frequency.items():
    print(f"{number} occurs {count} times")

Input	Expected	Got	
7
23
45
23
56
45
23
40
23 occurs 3 times
45 occurs 2 times
56 occurs 1 times
40 occurs 1 times
23 occurs 3 times
45 occurs 2 times
56 occurs 1 times
40 occurs 1 times

