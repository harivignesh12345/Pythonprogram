Write a program to calculate and print the Electricity bill where the unit consumed by the user is given from test case. It prints the total amount the customer has to pay. The charge are as follows: 

Unit                                                     Charge / Unit

Upto 199                                             @1.20

200 and above but less than 400        @1.50

400 and above but less than 600        @1.80

600 and above                                    @2.00

If bill exceeds Rs.400 then a surcharge of 15% will be charged and the minimum bill should be of Rs.100/- 

Sample Test Cases

Test Case 1 

Input

50 

Output

100.00 

Test Case 2

Input 

300

Output 

517.50



For example:

Input	Result
100.00
120.00
a=float(input())
if(a<200):
    b=1.20*a
elif(a>=200 and a<400):
    b=1.50*a
elif(a>=400 and a<600):
    b=1.80*a
else: 
    b=2.0*a
if(b<=100):
    print("100.00")
elif(b>400):
    c=0.15*b
    b=c+b
    print(f"{b:.2f}")
else:    
    print(f"{b:.2f}")
  Input	Expected	Got	
50
100.00
100.00
100.00
120.00
120.00
500
1035.00
1035.00
700
1610.00
1610.00

