Given a number with maximum of 100 digits as input, find the difference between the sum

of odd and even position digits.

Input Format:

Take a number in the form of String from stdin.

Output Format:

Print the difference between sum of even and odd digits

Example input:

1453

Output:

1

Explanation:

Here, sum of even digits is 4 + 3 = 7

sum of odd digits is 1 + 5 = 6.

Difference is 1.

Note that we are always taking absolute difference

 def differenceSum(n):
   odd=0
   even=0
   k=str(n)
   for i in range(len(k)):
       if i%2==0:
           odd=odd+int(k[i])
       else:  
           even+=int(k[i])
   return even-odd
Test	Expected	Got	
print(differenceSum(1453))
1
1
