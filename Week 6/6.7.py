Write a program to print all the locations at which a particular element (taken as input) is found in a list and also print the total number of times it occurs in the list. The location starts from 1.

 

For example, if there are 4 elements in the array:

 

5

6

5

7

 

If the element to search is 5 then the output will be:

 

5 is present at location 1

5 is present at location 3

5 is present 2 times in the array.

 

Sample Test Cases

 

Test Case 1

 

Input

 

4

5

6

5

7

5

 

Output

 

5 is present at location 1.

5 is present at location 3.

5 is present 2 times in the array.

 

Test Case 2

 

Input

 

5

67

80

45

97

100

50

 

Output

 

50 is not present in the array.

n=int(input())
element=[]
while(n):
    element.append(int(input()))
    n-=1
search=int(input())
l=len(element)
c=0

for i in range(l):
    if(element[i]==search ):
        print(f'{search} is present at location {i+1}.')
        c=c+1
    else: 
        continue
if(c==0):
    print(f'{search} is not present in the array.')
else:
    print(f'{search} is present {c} times in the array.')
  Input	Expected	Got	
4
5
6
5
7
5
5 is present at location 1.
5 is present at location 3.
5 is present 2 times in the array.
5 is present at location 1.
5 is present at location 3.
5 is present 2 times in the array.
5
67
80
45
97
100
50
50 is not present in the array.
50 is not present in the array.
