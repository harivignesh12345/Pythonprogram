Reverse a string without affecting special characters
 Given a string S, containing special characters and all the alphabets, reverse the string without affecting the positions of the special characters.
Input:
A&B
Output:
B&A
Explanation: As we ignore '&' and
As we ignore '&' and then reverse, so answer is "B&A".


For example:

Input	Result
A&x#
x&A#
s=input()
L=[]
for k in s:
    L.append(k)
j=len(L)-1
i=0
while(not(i==j)):
    if(L[i].isalnum()):
        while(not(L[j].isalnum())):
            j-=1
        temp=L[i]
        L[i]=L[j]
        L[j]=temp
        j-=1
        i+=1
    else:
        i+=1
        continue
s=""
for k in L:
    s+=k
print(s)
Input	Expected	Got	
A&B
B&A
B&A
