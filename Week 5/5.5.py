Robert  is having 2 strings consist of uppercase & lowercase english letters. Now he want to compare those two strings lexicographically. The letters' case does not matter, that is an uppercase letter is considered equivalent to the corresponding lowercase letter.


Input
The first line contains T. Then T test cases follow.

Each test case contains a two lines contains a string. The strings' lengths range from 1 to 100 inclusive. It is guaranteed that the strings are of the same length and also consist of uppercase and lowercase Latin letters.

Output
If the first string is less than the second one, print "-1".
If the second string is less than the first one, print "1".
If the strings are equal, print "0".
Note that the letters' case is not taken into consideration when the strings are compared.

Constraints
                      1≤T≤50
                      String length≤100

For example:

Input	Result
3
aaaa
aaaA
abs
Abz
abcdefg
AbCdEfF
0
-1
1
T= int(input())
for i in range(T):
    
    
    s1 = input()
    s2 = in
  str1 = s1.lower()
    str2 = s2.lower()

    if str1 < str2:
        print("-1")
    elif str1 > str2:
        print("1")
    else:
        print("0")
  Input	Expected	Got	
3
aaaa
aaaA
abs
Abz
abcdefg
AbCdEfF
0
-1
1
0
-1
1

