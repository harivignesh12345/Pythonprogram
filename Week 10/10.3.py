To find the frequency of numbers in a list and display in sorted order.

Constraints: 

1<=n, arr[i]<=100 

Input: 

1 68 79 4 90 68 1 4 5 

output:

 1 2

 4 2

 5 1

 68 2

 79 1 

90 1


For example:

Input	Result
4 3 5 3 4 5
3 2
4 2
5 2

 from collections import Counter

# Get list of numbers from user
arr = input().split()
arr = [int(x) for x in arr]

# Count frequency of each number
freq = Counter(arr)

# Sort the frequency dictionary by key
sorted_freq = dict(sorted(freq.items()))

# Print the frequency of each number in sorted order
for key, value in sorted_freq.items():
    print(f"{key} {value}")

Input	Expected	Got	
4 3 5 3 4 5
3 2
4 2
5 2
3 2
4 2
5 2
12 4 4 4 2 3 5
2 1
3 1
4 3
5 1
12 1
2 1
3 1
4 3
5 1
12 1
5 4 5 4 6 5 7 3
3 1
4 2
5 3
6 1
7 1
3 1
4 2
5 3
6 1
7 1
