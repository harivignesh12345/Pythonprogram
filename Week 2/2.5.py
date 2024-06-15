Mr. X's birthday is in next month. This time he is planning to invite N of his friends. He wants to distribute some chocolates to all of his friends after the party. He went to a shop to buy a packet of chocolates. At the chocolate shop, 4 packets are there with different numbers of chocolates. He wants to buy such a packet which contains a number of chocolates, which can be distributed equally among all of his friends. Help Mr. X to buy such a packet.

 Input Given: 

N-No of friends

P1,P2,P3 AND P4-No of chocolates

OUTPUT:

 "True" if he can buy that packet and "False" if he can't buy that packet.

SAMPLE INPUT AND OUTPUT:

5

25

12  

10  

9

OUTPUT

True False True False
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
print(f"{bool(b%a==0)} {bool(c%a==0)} {bool(d%a==0)} {bool(e%a==0)}")
Input	Expected	Got	
5
25
23
20
10
True False True True
True False True True
4
23
24
21
12
False True False True
False True False True
8
64
8
16
32
True True True True
True True True True

