Program to print all the distinct elements in an array. Distinct elements are nothing but the unique (non-duplicate) elements present in the given array.

Input Format:

First line take an Integer input from stdin which is array length n.

Second line take n Integers which is inputs of array.

Output Format:

Print the Distinct Elements in Array in single line which is space Separated

Example Input:

5

1 

2 

2 

3 

4

Output:

1 2 3 4

Example Input:

6

1 

1 

2 

2 

3 

3

Output:

1 2 3


For example:

Input	Result
5
1 
2 
2 
3
4
1 2 3 4 
6
1 
1 
2 
2 
3 
3
1 2 3 
n=int(input())
x=[]
for i in range(0,n):
    a=int(input())
    x.append(a)
p=list(set(x))
P=' '.join(str(i) for i in p)
print(P) 

Input	Expected	Got	
5
1
2
2
3
4
1 2 3 4
1 2 3 4
6
1
1
2
2
3
3
1 2 3
1 2 3
