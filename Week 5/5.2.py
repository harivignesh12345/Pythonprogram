Two string values S1, S2 are passed as the input. The program must print first N characters present in S1 which are also present in S2.

Input Format:

The first line contains S1.
The second line contains S2.
The third line contains N.

Output Format:

The first line contains the N characters present in S1 which are also present in S2.

Boundary Conditions:

2 <= N <= 10
2 <= Length of S1, S2 <= 1000

Example Input/Output 1:
  

Input:

abcbde
cdefghbb
3

Output:

bcd

Note:

b occurs twice in common but must be printed only once.
  S1 = input()
S2 = input()
N=int(input())
common_chars = set()

for char in S1:
    if char in S2:
        common_chars.add(char)

print(''.join(sorted(common_chars)[:N]))
Input	Expected	Got	
abcbde
cdefghbb
3
bcd
bcd
