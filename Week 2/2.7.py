Write a python program that takes a integer between 0 and 15 as input and displays the number of '1' s in its binary form.(Hint:use python bitwise operator.

Sample Input

3

Sample Output:

2

Explanation:

The binary representation of 3 is 011, hence there are 2 ones in it. so the output is 2.


For example:

Input	Result
3
2
a=int(input())
b=str(bin(a))
c=b.count("1")
print(c)
Input	Expected	Got	
3
2
2
5
2
2
15
4
4
