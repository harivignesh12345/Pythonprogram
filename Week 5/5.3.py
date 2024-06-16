Given two Strings s1 and s2, remove all the characters from s1 which is present in s2.

 

Constraints

 

1<= string length <= 200

 

Sample Input 1

 

experience

enc

 

Sample Output 1

 

xpri
n1=input()
n2=input()

n=len(n1)
a=len(n2)
s=""
for i in n1:
    if(not(i in n2)):
        s+=i



print(s)         
Input	Expected	Got	
experience
enc
xpri
xpri
