In London, every year during Dasara there will be a very grand doll show. People try to invent new dolls of different varieties. The best-sold doll's creator will be awarded with a cash prize. So people broke their heads to create dolls innovatively. Knowing this competition, Mr.Lokpaul tried to create a doll that sings only when an even number is pressed and the number should not be zero and greater than 100.

 IF Lokpaul wins print true, otherwise false.

Sample Input

10

Sample Output

True

Explanation:

Since 10 is an even number and a number between 0 and 100, True is printed



For example:

Input	Result
101
False
Answer:(penalty regime: 0 %)
a=int(input())
if(a>0 & a<101):
 if(a%2==0):
     print("True")
 else:
     print("False")
else:
 print("False")
 
Input	Expected	Got	
56
True
True
101
False
False
-1
False
False
Passed all tests!  
