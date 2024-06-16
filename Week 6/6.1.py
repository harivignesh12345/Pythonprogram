Given an array A of sorted integers and another non negative integer k, find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.

Input Format

1.      First line is number of test cases T. Following T lines contain:

2.      N, followed by N integers of the array

3.      The non-negative integer k

Output format

Print 1 if such a pair exists and 0 if it doesn’t.

Example

Input

1

3 

1 

3 

5

4

Output:

1

Input

1

3 

1 

3 

5

99

Output

0


For example:

Input	Result
1
3 
1 
3 
5
4
1
1
3 
1 
3 
5
99
0
T=int(input())
while(T):
    flag=False
    n=int(input())
    L=[]
    while(n):
        L.append(int(input()))
        n-=1
    k=int(input())
    for i in range(0,len(L)):
        for j in range(0,len(L)):
            if(not(i==j) and (L[i]-L[j]==k)):
                flag=True
                break
        if(flag):
            break
    if(flag):
        print(1)
    else:
        print(0)
    T=T-1
Input	Expected	Got	
1
3
1
3
5
4
1
1
1
3
1
3
5
99
0
0
