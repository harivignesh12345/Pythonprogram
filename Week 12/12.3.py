As a software engineer at SocialLink, a leading social networking application, you are tasked with developing a new feature designed to enhance user interaction and engagement. The company aims to introduce a system where users can form connections based on shared interests and activities. One of the feature's components involves analyzing pairs of users based on the activities they've participated in, specifically looking at the numerical difference in the number of activities each user has participated in.

Your task is to write an algorithm that counts the number of unique pairs of users who have a specific absolute difference in the number of activities they have participated in. This algorithm will serve as the backbone for a larger feature that recommends user connections based on shared participation patterns.

Problem Statement

Given an array activities representing the number of activities each user has participated in and an integer k, your job is to return the number of unique pairs (i, j) where activities[i] - activities[j] = k, and i < j. The absolute difference between the activities should be exactly k.

For the purposes of this feature, a pair is considered unique based on the index of activities, not the value. That is, if there are two users with the same number of activities, they are considered distinct entities.

Input Format

The first line contains an integer, n, the size of the array nums.

The second line contains n space-separated integers, nums[i].

The third line contains an integer, k.


Output Format

Return a single integer representing the number of unique pairs (i, j) 

where | nums[i] - nums[j] | = k and i < j.


Constraints:

1 ≤ n ≤ 105

-104 ≤ nums[i] ≤ 104

0 ≤ k ≤ 104



For example:

Input	Result
5
1 3 1 5 4
0
1
4
1 2 2 1
1
4
 i=int(input())
j=input().split(" ")
k=int(input())
c=0
for t in range(i):
 
 for a in range(t+1,i):
  if abs(int(j[t])-int(j[a]))==k:
   c+=1
print(
Input	Expected	Got	
4
1 2 3 4
1
3
3
5
1 3 1 5 4
0
1
1
4
1 2 2 1
1
4
4
