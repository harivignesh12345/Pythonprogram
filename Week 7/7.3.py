Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

 

Example 1:

Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]
Example 2:

Input: words = ["omk"]
Output: []
Example 3:

Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]


For example:

Input	Result
4
Hello
Alaska
Dad
Peace
Alaska
Dad
2
adsfd
afd
adsfd
afd

n=int(input())
L=[]
while(n):
    L.append(input())
    n-=1
K=["qwertyuiop","asdfghjkl","zxcvbnm"]
Y={}
for i in K:
    Y[i]=[]
for k in K:
    for l in L:
        if(set(k).union(set(l.lower()))==set(k)): #if the word can be typed using 1 row of keyboard then the union of the word and the row of keyboard is the row of keyboard
            Y[k].append(l)
        else:
            continue
flag=True
for m in Y:
    if(Y[m]==[]):
        continue
    else:
        flag=False
        break
if(not(flag)):
    for x in Y:
        for s in Y[x]:
            print(s)
else:
    print("No words")
  Input	Expected	Got	
4
Hello
Alaska
Dad
Peace
Alaska
Dad
Alaska
Dad
1
omk
No words
No words
2
adsfd
afd
adsfd
afd
adsfd
afd
