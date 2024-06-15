Most years have 365 days. However, the time required for the Earth to orbit the Sun is actually slightly more than that. As a result, an extra day, February 29, is included in some years to correct for this difference. Such years are referred to as leap years. The rules for determining whether or not a year is a leap year follow:

• Any year that is divisible by 400 is a leap year.

• Of the remaining years, any year that is divisible by 100 is not a leap year.

• Of the remaining years, any year that is divisible by 4 is a leap year.

• All other years are not leap years.

Write a program that reads a year from the user and displays a message indicating whether or not it is a leap year.

Sample Input 1

1900

Sample Output 1

1900 is not a leap year.

Sample Input 2

2000

Sample Output 2

2000 is a leap year
a=int(input())
if(a%400==0):
    print(f"{a} is a leap year.")
elif(a%100==0):
    print(f"{a} is not a leap year.")
elif(a%4==0):
    print(f"{a} is a leap year.")
else:
    print(f"{a} is not a leap year.")
  Input	Expected	Got	
1900
1900 is not a leap year.
1900 is not a leap year.
2000
2000 is a leap year.
2000 is a leap year.
2100
2100 is not a leap year.
2100 is not a leap year.
2400
2400 is a leap year.
2400 is a leap year.
