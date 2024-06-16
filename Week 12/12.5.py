Given an integer n, print true if it is a power of four. Otherwise, print false.

An integer n is a power of four, if there exists an integer x such that n == 4x.

For example:

Input	Result
16
True
5
False
n=int(input())
print(n>0 and (n&(n-1))==0 and (n&0x55555555)!=0)
 

Input	Expected	Got	
16
True
True
5
False
False
1
True
True
-1
False
False
